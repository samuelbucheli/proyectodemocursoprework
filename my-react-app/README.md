##### 项目搭建

1. 基于 CRA + react-app-rewired + customize-cra
2. 兼容只支持 es2015([caniuse](https://www.caniuse.com/#search=es6))以上的现代浏览器
3. 引入 lodash
4. 引入 normalize.css--对 css 进行重写, 可以与 reset.css 进行参考对比

##### 特性说明

1. 配置简化路径如"@/", 需同时在 config-overriders.js 与 tsconfig.paths.json 中配置
2. mock 内 json 文件需与 setupProxy.js 对应, 反向代理在此文件内写入
3. mock 采用 express 最简单实现, 通过 yarn mock 启动, 数据代理通过 src/setupProxy.js 进行配置
4. CRA 支持组件化引入矢量图 如 import { ReactComponent as Logo } from './logo.svg'; @see[svg](https://create-react-app.dev/docs/adding-images-fonts-and-files#adding-svgs), 自定义 icon 可以通过此种方式进行引入

##### 项目考虑

1. 项目目录及模块化划分

```tree

```

2. 共用与复用

    1. 公共组件

        基于 antd 为基础组件库, 减少公共组件, 需考虑功能与概念上一致; 通过一定量的重复 jsx 代码, 降低复杂度与增强后期需求适应性

    2. 公共状态

        考虑到中途用户可能有刷新动作, 常规解决方案为, 保存到本地, 刷新后读取到 store;

        把路由组件(一级或二级)设置为容器性组件, 此处设置公共状态获取, 用户刷新时自然会去请求相应状态, 减少本地存储, 降低复杂度;

    3. 代码逻辑复用

        优先考虑代码逻辑复用, 通过 HOC/hooks 进行实现

3. 性能优化

    1. 静态资源
         
       webpack 处理

    2. 运行时

        1. 大 Task --> 小 Task [Idle Until Urgent](https://philipwalton.com/articles/idle-until-urgent/)
        2. ...

4. git 工作流

    暂未添加

5. 前端监控

    暂未添加

6. store 定位

    1. store 文件命名应与组件或模块名一致, 但采用小驼峰;
    2. 尽量通过属性传值/context 传值
    3. 只有公共引用时才有必要放置到 store 内

7. 美杜莎

    采用 local 配置, 相关内容在 gitlab-ci.yml 与 med 文件夹内;
    在测试环境下, 默认支持 source-map;
    线上环境下, source-map 关闭;

8. 命名规范

    1. 文件命名 -- 组件文件采用大驼峰, 其余应采用小驼峰
    2. css 样式
        1. 使用 css-module 方式时, 文件名应为 example.module.less, 应采用小驼峰方式明明
        2. 使用正常引入方式时, 文件名正常, 应采用中划线分割, 注意命名, 防止全局命名冲突造成的影响; 建议 moduleName-componentName-currentComponentName...

9. 代码规范

    1. 风格校验--采用 prettier 处理
    2. 质量校验--除部分为了应用 eslint 校验 ts 之外, 采用 airbnb 规范

##### 一些问题
