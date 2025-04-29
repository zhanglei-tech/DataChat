import { type App } from 'vue'
import HelloWorld from './HelloWorld.vue'

export default {
  install(app: App) {
    app.component('HelloWorld', HelloWorld)
  }
}