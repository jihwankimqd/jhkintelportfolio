module.exports = {
    publicPath: '/intelportfolio/',

    pages: {
      'index': {
        entry: './src/pages/Home/main.js',
        template: 'public/index.html',
        title: 'Home',
        chunks: [ 'chunk-vendors', 'chunk-common', 'index' ]
      },
      'about': {
        entry: './src/pages/About/main.js',
        template: 'public/index.html',
        title: 'About',
        chunks: [ 'chunk-vendors', 'chunk-common', 'about' ]
      },
      'portfolio': {
        entry: './src/pages/Portfolio/main.js',
        template: 'public/index.html',
        title: 'Portfolio',
        chunks: [ 'chunk-vendors', 'chunk-common', 'portfolio' ]
      },
      'dashboard': {
        entry: './src/pages/Dashboard/main.js',
        template: 'public/index.html',
        title: 'Dashboard',
        chunks: [ 'chunk-vendors', 'chunk-common', 'dashboard' ]
      },
      'projects': {
        entry: './src/pages/Projects/main.js',
        template: 'public/index.html',
        title: 'Projects',
        chunks: [ 'chunk-vendors', 'chunk-common', 'projects' ]
      }
    }
  }