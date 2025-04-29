import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import Components from '@/components'

const app = createApp(App)
app.use(Components)
app.mount('#app')
export { app }
