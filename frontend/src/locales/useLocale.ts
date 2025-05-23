import { useLocalStorage } from '@vueuse/core';
import { computed } from 'vue';
import { useI18n } from 'vue-i18n';

import { i18n, langCode, localeConfigKey } from '@/locales/index';

export function useLocale() {
    const { locale } = useI18n({ useScope: 'global' });
    function changeLocale(lang: string) {
        // 如果切换的语言不在对应语言文件里则默认为简体中文
        if (!langCode.includes(lang)) {
            lang = 'zh-CN';
        }

        locale.value = lang;
        useLocalStorage(localeConfigKey, 'zh-CN').value = lang;
    }

    const getComponentsLocale = computed(() => {
        const messages = i18n.global.getLocaleMessage(locale.value) as any;
        return messages?.componentsLocale || {};
    });

    return {
        changeLocale,
        getComponentsLocale,
        locale,
    };
}
