### Back End API

For production change the following

	src/constants.ts/__BASE_URL__
	src/constants.ts/__MODEL_URL__

### Using the API

```typescript
// endpoint: METHOD => POST
'/api/predict';

// Input: application/json
image: TensorLike2D;

// Output: application/json
classification: 'positive' | 'negative';
probability: number;
```
