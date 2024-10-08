import { oakCors } from 'https://deno.land/x/cors@v1.2.2/mod.ts';
import { Application } from 'https://deno.land/x/oak@v12.4.0/mod.ts';
import { router } from './router.ts';

const app = new Application();
const PORT = 8000;

app.use(oakCors()); // TODO: Dangerous?
app.use(router.routes());
app.use(router.allowedMethods());

console.log(`Listening on port ${PORT}`);
await app.listen({ port: PORT });
