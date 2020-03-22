<template>
    <v-app>
        <v-navigation-drawer v-model="drawer" app clipped>
            <v-list dense>
                <v-list-item @click="articleDialog = true">
                    <v-list-item-action>
                        <v-icon>cloud_upload</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                        <v-list-item-title>Submit Article</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
            </v-list>
        </v-navigation-drawer>
        <v-app-bar app dark clipped-left>
            <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
            <v-toolbar-title class="headline text-uppercase">
                <span class="blue--text">
                    <v-icon class="blue--text" style="font-size: 38px;">face</v-icon>Chadev
                </span>
                <span class="font-weight-light red--text">Monster</span>
            </v-toolbar-title>
            <v-spacer />
            <v-flex xs12 md4>
                <v-text-field v-model="search" append-icon="search" label="Search" single-line hide-details />
            </v-flex>
        </v-app-bar>

        <v-content>
            <template>
                <v-data-table
                    dense
                    :headers="headers"
                    :search="search"
                    :items="articles"
                    item-key="article_id"
                    class="elevation-1"
                    :items-per-page="25"
                />
            </template>
        </v-content>

        <ArticleForm :article-dialog.sync="articleDialog" @close-dialog="articleDialog = false" />
    </v-app>
</template>

<script>
import ArticleForm from "./components/ArticleForm"

export default {
    name: "App",
    components: {
        ArticleForm
    },
    data: () => ({
        drawer: false,
        articleDialog: false,
        search: "",
        articles: [],
        headers: [
            {
                text: "ID",
                align: "left",
                sortable: false,
                value: "id"
            },
            { text: "Name", value: "title" },
            { text: "URL", value: "url" }
        ]
    }),
    created() {
        this.$chadevmonster_api
            .get("articles")
            .then(async response => {
                this.articles = response.data
                // response.data.forEach(element => {
                //     console.log("element:", element)
                // })
            })
            .catch(error => {
                console.log("error", error)
            })
    }
}
</script>
