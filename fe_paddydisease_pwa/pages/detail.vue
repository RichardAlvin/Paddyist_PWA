<template>
  <main class="site-main">
    <section class="detail">
      <div class="container">
        <div class="row">
            <div class="col-8 col-md-10 col-sm-9">
                <h2>{{dataDisease.title}}</h2>
            </div>
            <div class="col-4 col-md-2 col-sm-3">
                <div>
                    <b-button href="/penyakit-padi">Kembali</b-button>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-12 m-auto">
                <div class="owl-carousel owl-theme">
                    <h3>Carousel</h3>
                </div>
            </div>
        </div>
        <p>PublishedAt: {{dataDisease.created_at}}</p>
        <p>{{dataDisease.body}}</p>
      </div>
    </section>
  </main>
</template>

<script>
// import 'vue-slick-carousel/dist/vue-slick-carousel.css'
export default {
  name: 'IndexPage',
  data() {
    return {
      dataDisease: []
    }
  },
  async fetch() {
    await this.$axios.get(`${this.$apiurl()}/disease/normal`)
      .then((res) => {
        this.dataDisease = res.data
        // this.dataBanner = res[0].data[0]
      })
      .catch((error) => {
        // eslint-disable-next-line no-console
        console.log(error.response)
      })
  },
}
</script>

<style lang="scss" scoped>
.detail{
    padding-top:25px;
}
</style>
