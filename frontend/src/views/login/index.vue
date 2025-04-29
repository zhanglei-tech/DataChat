<template>
  <div class="login-warp flex-center">
    <div class="login-container w-full h-full">
      <el-row class="container w-full h-full">
        <el-col :xs="0" :sm="0" :md="12" :lg="1120" :xl="12" class="left-container">
          <div class="login-image"></div>
        </el-col>
        <el-col :xs="24" :sm="24" :md="12" :lg="12" :xl="12" class="right-container">
          <div class="flex-center" style="height: 100vh">
            <div class="login-form-container">
              <div class="login-title">
                <div class="logo text-center">
                  <img src="@/assets/vue.svg" height="45px" />
                </div>
                <div class="sub-title text-center">
                  <el-text type="info">{{ $t('system.defaultSlogan') }}</el-text>
                </div>
              </div>
              <el-card class="login-card">
                <h2 class="mb-24">{{ $t('views.login.title') }}</h2>
                <div>
                  <el-form
                    class="login-form"
                    :rules="rules"
                    :model="loginForm"
                    ref="loginFormRef"
                    @keyup.enter="login"
                  >
                    <div class="mb-24">
                      <el-form-item prop="username">
                        <el-input
                          size="large"
                          class="input-item"
                          v-model="loginForm.username"
                          :placeholder="$t('views.login.placeholder.username')"
                        >
                        </el-input>
                      </el-form-item>
                    </div>
                    <div class="mb-24">
                      <el-form-item prop="password">
                        <el-input
                          type="password"
                          size="large"
                          class="input-item"
                          v-model="loginForm.password"
                          :placeholder="$t('views.login.placeholder.password')"
                          show-password
                        >
                        </el-input>
                      </el-form-item>
                    </div>
                  </el-form>

                  <el-button size="large" type="primary" class="w-full" @click="login"
                    >{{ $t('views.login.buttons.login') }}
                  </el-button>
                  <div class="operate-container flex-between mt-12">
                    <el-button
                      class="forgot-password"
                      @click="router.push('/forgot_password')"
                      link
                      type="primary"
                    >
                      {{ $t('views.login.forgotPassword') }}?
                    </el-button>
                  </div>
                </div>
              </el-card>
            </div>
          </div>
        </el-col>
      </el-row>
   </div>
  </div>
</template>
<script setup lang="ts">
import { onMounted, ref, onBeforeMount } from 'vue'
import { useRouter } from 'vue-router'
import type { FormInstance } from 'element-plus'
import { t } from '@/locales'

const loading = ref<boolean>(false)
const router = useRouter()
const loginForm = {
  username: '',
  password: ''
}

const rules = {
  username: [
    {
      required: true,
      message: t('views.user.userForm.form.username.requiredMessage'),
      trigger: 'blur'
    }
  ],
  password: [
    {
      required: true,
      message: t('views.user.userForm.form.password.requiredMessage'),
      trigger: 'blur'
    }
  ]
}
const loginFormRef = ref<FormInstance>()

const login = () => {
  loginFormRef.value?.validate().then(() => {

  })
}

onBeforeMount(() => {

})

onMounted(() => {
})
</script>

<style lang="scss" scoped>
.login-warp {
  height: 100vh;

  .login-image {
    background: url(@/assets/login-bg.png);
    background-repeat: no-repeat;
    background-position: center;
    background-size: cover;
    width: 100%;
    height: 100%;
  }
  .right-container {
    position: relative;
    .lang {
      position: absolute;
      right: 20px;
      top: 20px;
    }
  }

  .login-form-container {
    width: 480px;

    .login-title {
      margin-bottom: 32px;
      .sub-title {
        font-size: 16px;
      }
    }
    .login-card {
      border-radius: 8px;
      padding: 18px;
    }

    .login-gradient-divider {
      position: relative;
      text-align: center;
      color: var(--el-color-info);

      ::before {
        content: '';
        width: 25%;
        height: 1px;
        background: linear-gradient(90deg, rgba(222, 224, 227, 0) 0%, #dee0e3 100%);
        position: absolute;
        left: 16px;
        top: 50%;
      }

      ::after {
        content: '';
        width: 25%;
        height: 1px;
        background: linear-gradient(90deg, #dee0e3 0%, rgba(222, 224, 227, 0) 100%);
        position: absolute;
        right: 16px;
        top: 50%;
      }
    }

    .login-button-circle {
      padding: 20px !important;
      margin: 0 4px;
      width: 32px;
      height: 32px;
      text-align: center;
    }
  }
}

</style>
