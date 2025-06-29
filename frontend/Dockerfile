# Stage 1: Build
FROM node:22-alpine AS builder

ARG NUXT_PUBLIC_API_BASE
ENV NUXT_PUBLIC_API_BASE=$NUXT_PUBLIC_API_BASE

# pnpm installieren
RUN corepack enable && corepack prepare pnpm@latest --activate

WORKDIR /app

# Nur package-Dateien kopieren
COPY pnpm-lock.yaml package.json ./

# Abhängigkeiten installieren
RUN pnpm install

# Projektdateien kopieren
COPY . .

# Nuxt-App bauen
RUN pnpm build

# Stage 2: Production
FROM node:22-alpine AS production

# pnpm wieder aktivieren (für Runtime-Abhängigkeiten)
RUN corepack enable && corepack prepare pnpm@latest --activate

WORKDIR /app

# Nur Production-Abhängigkeiten installieren
COPY pnpm-lock.yaml package.json ./
RUN pnpm install --prod

# Nur das Nuxt-Output-Verzeichnis kopieren
COPY --from=builder /app/.output ./

EXPOSE 3000

CMD ["node", "server/index.mjs"]
