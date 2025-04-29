<template>
  <login-layout v-if="!loading" v-loading="loading">
    <LoginContainer subTitle="欢迎使用智能问数系统">
      <h2 class="mb-24">普通登录</h2>
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
                placeholder="请输入用户名"
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
                placeholder="请输入密码"
                show-password
              >
              </el-input>
            </el-form-item>
          </div>
        </el-form>

        <el-button size="large" type="primary" class="w-full" @click="login">登录</el-button>
        <div class="operate-container flex-between mt-12">
          <el-button
            class="forgot-password"
            @click="router.push('/forgot_password')"
            link
            type="primary"
          >
            忘记密码？
          </el-button>
        </div>
      </div>
    </LoginContainer>
  </login-layout>
</template>
<script setup lang="ts">
import { onMounted, ref, onBeforeMount } from 'vue'
import { useRouter } from 'vue-router'
import type { FormInstance } from 'element-plus'

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
      message: '请输入用户名',
      trigger: 'blur'
    }
  ],
  password: [
    {
      required: true,
      message: '请输入密码',
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
</style>
