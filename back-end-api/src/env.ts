import dotenv from 'dotenv';
import { cleanEnv, str, num } from 'envalid';

dotenv.config();

const env = cleanEnv(process.env, {
  NODE_ENV: str({
    choices: ['development', 'production', 'test'],
    default: 'development',
  }),
  PORT: num({ default: 5000 }),
  CLIENT_URL: str({ default: 'http://localhost:3000' }),
});

export default env;
