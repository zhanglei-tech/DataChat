import '@/style.css'
import ElementPlus from 'element-plus'
import * as ElementPlusIcons from '@element-plus/icons-vue'
import { createApp } from 'vue'
import App from './App.vue'
import router from '@/router'
import Components from '@/components'

const app = createApp(App)

for (const [key, component] of Object.entries(ElementPlusIcons)) {
  app.component(key, component)
}

app.use(ElementPlus)
  
app.use(router)
app.use(Components)
app.mount('#app')
export { app }
