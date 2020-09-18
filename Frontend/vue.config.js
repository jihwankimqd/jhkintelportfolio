module.exports = {
    publicPath: '/intelportfolio/',

    pages: {
      'index': {
        entry: './src/pages/Home/main.js',
        template: 'public/index.html',
        title: 'Home',
        chunks: [ 'chunk-vendors', 'chunk-common', 'index' ]
      },
      'portfolio': {
        entry: './src/pages/Portfolio/main.js',
        template: 'public/index.html',
        title: 'Portfolio',
        chunks: [ 'chunk-vendors', 'chunk-common', 'portfolio' ]
      }
    }
  }