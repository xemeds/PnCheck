import express, { Request, Response, NextFunction } from 'express';

import * as tf from '@tensorflow/tfjs';
import cors from 'cors';

import env from './env';
import { errorMiddleware, HttpException } from './middleware/error';
import { __MODEL_URL__, __PREDICTION_NUMBER__ } from './constants';

class Server {
  private app: express.Application;
  private PORT: number;
  private model: any;

  constructor() {
    this.app = express();
    this.PORT = env.PORT;
    this.model = this.configuration();
    this.routes();
    this.error();
  }

  public configuration() {
    this.app.use(express.json({ limit: '50mb' }));
    this.app.use(cors());
  }

  private async loadModel() {
    const model = await tf.loadLayersModel(__MODEL_URL__);
    return model;
  }

  public routes() {
    this.app.get('/', (_req: Request, res: Response, _next: NextFunction) => {
      return res.status(200).json({
        message: 'Welcome to the PnCheck Prediction API',
        status: 200,
      });
    });

    this.app.post(
      '/api/predict',
      async (req: Request, res: Response, next: NextFunction) => {
        try {
          if (!this.model) this.model = await this.loadModel();
          const image = req.body?.image;
          const imageSize = [1, 128, 128, 1];

          const processedImage = tf.tensor2d(image);
          const predict = this.model.predict(
            tf.reshape(processedImage, imageSize),
          );
          // const label = predict.argMax(1).get([0]);

          const predictionValue = predict?.dataSync()?.[0];

          return res.status(200).json({
            classification:
              predictionValue > __PREDICTION_NUMBER__ ? 'positive' : 'negative',
            probability: predictionValue,
          });
        } catch (error) {
          return next(error);
        }
      },
    );
  }

  private error() {
    this.app.use((_req: Request, _res: Response, next: NextFunction) => {
      const error = new Error('Not Found');
      (error as HttpException).status = 404;
      next(error);
    });
    this.app.use(errorMiddleware);
  }

  public start() {
    this.app.listen(this.PORT, () => {
      console.log(`App started in ${env.NODE_ENV} mode on port ${this.PORT}`);
    });
  }
}

const server = new Server();
server.start();

export default server;
