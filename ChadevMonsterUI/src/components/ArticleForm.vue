<template>
    <v-layout justify-center>
        <v-dialog v-model="articleDialog" persistent max-width="600px">
            <v-card>
                <v-card-title>
                    <span class="headline">New Article</span>
                </v-card-title>
                <v-card-text>
                    <v-subheader>All submissions are subject to approval</v-subheader>
                    <v-container grid-list-md>
                        <v-layout wrap>
                            <v-flex xs12>
                                <v-form ref="form" enctype="multipart/form-data">
                                    <v-flex>
                                        <v-text-field
                                            v-model="title"
                                            label="Article Title"
                                            hint="Original title of the article"
                                        />
                                    </v-flex>
                                    <v-flex>
                                        <v-text-field
                                            v-model="url"
                                            label="Article URL"
                                            hint="URL must not contain referral codes"
                                        />
                                    </v-flex>
                                </v-form>
                            </v-flex>
                        </v-layout>
                    </v-container>
                </v-card-text>
                <v-card-actions>
                    <v-spacer />
                    <v-btn color="blue darken-1" text @click="$emit('close-dialog')">Close</v-btn>
                    <v-btn color="blue darken-1" text @click="submitArticle()">Save</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </v-layout>
</template>

<script>
import axios from "axios"

export default {
    props: {
        articleDialog: Boolean
    },
    data: () => ({
        title: "",
        url: ""
    }),
    methods: {
        submitArticle: function() {
            if (this.$refs.form.validate()) {
                this.$emit("close-dialog")

                let article_object = {
                    article_url: this.url,
                    article_title: this.title
                }

                this.$chadevmonster_api
                    .post("articles", article_object)
                    .then(async response => {
                        console.log("response:", response)
                        // emit a load of all articles on the app.vue file
                    })
                    .catch(error => {
                        console.log("error", error)
                    })
            }
        }
    }
}
</script>
