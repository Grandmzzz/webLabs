<template>
  <div class="body">
    <!-- BEGIN wrapper -->
    <div id="header">
        <!-- begin pages -->
        <ul class="pages">
            <li><router-link to="/">Home</router-link></li>
            <li><router-link to="/about">About Us</router-link></li>
            <li><router-link to="/page">Demo Page</router-link></li>
            <li><router-link to="/authorization">Enter Page</router-link></li>
            <li><router-link to="/registration">Registration</router-link></li>
        </ul>
        <!-- end pages -->
        <form action="#">
        <input type="text" name="s" id="s" value="" />
        <button type="submit">Search</button>
        </form>
        <div class="break"></div>
        <!-- begin logo -->
        <div class="logo">
            <h1><router-link to="/">SimpleScheme Magazine</router-link></h1>
            <p>Free CSS Template</p>
        </div>
        <!-- end logo -->
        <!-- begin sponsor -->
        <div class="sponsor"> <a href="#"><img src="images/ad468x60.gif" alt="" /></a> </div>
        <!-- end sponsor -->
    </div>
    <!-- END header -->
  </div>
</template>

<script>
export default {
    name: "Header",
    data (){
        return{
            title: 'Header'
        }
    }
}
</script>

