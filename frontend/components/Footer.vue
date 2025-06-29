<template>
  <div class="container-fluid mt-5">
    <footer
      class="d-flex flex-wrap justify-content-between align-items-center py-3 my-4 border-top text-info"
    >
      <p class="col-md-4 mb-0">© 2023 MOTfromH</p>
      <NuxtLink
        to="/"
        class="col-md-4 d-flex align-items-center justify-content-center mb-3 mb-md-0 me-md-auto link-dark text-decoration-none"
      >
        <img
          src="/public/images/logo_transparent.png"
          alt="Logo"
          style="height: 40px; width: auto"
        />
      </NuxtLink>
      <ul class="nav col-md-4 justify-content-end">
        <li class="nav-item">
          <NuxtLink to="/" class="nav-link px-2">Home</NuxtLink>
        </li>
        <li class="nav-item">
          <NuxtLink to="/datenschutz" class="nav-link px-2"
            >Datenschutz</NuxtLink
          >
        </li>
      </ul>
    </footer>
  </div>
</template>
