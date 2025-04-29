import '@/styles/index.scss'
// import '@/style.css'
import ElementPlus from 'element-plus'
import * as ElementPlusIcons from '@element-plus/icons-vue'
import zhCn from 'element-plus/dist/locale/zh-cn.mjs'
import enUs from 'element-plus/dist/locale/en.mjs'
import zhTW from 'element-plus/dist/locale/zh-tw.mjs'
import { createApp } from 'vue'
import App from './App.vue'
import router from '@/router'
import Components from '@/components'
import i18n from '@/locales'

const app = createApp(App)

for (const [key, component] of Object.entries(ElementPlusIcons)) {
  app.component(key, component)
}

const locale_map: any = {
  'zh-CN': zhCn,
  'zh-Hant': zhTW,
  'en-US': enUs
}
app.use(ElementPlus, {
  locale: locale_map[localStorage.getItem('DataChat-locale') || navigator.language || 'zh-CN']
})
  
app.use(router)
app.use(i18n)
app.use(Components)
app.mount('#app')
export { app }
