<template>
    <v-app>
        <v-navigation-drawer v-model="drawer" app clipped>
            <v-list dense>
                <v-list-item @click="uploadDialog = true">
                    <v-list-item-action>
                        <v-icon>cloud_upload</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                        <v-list-item-title>Upload new csv</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
                <v-list-item @click="donations = removedAnonymous">
                    <v-list-item-action>
                        <v-icon>person_add_disabled</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                        <v-list-item-title>Remove Anonymous</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
                <v-list-item @click>
                    <v-list-item-action>
                        <v-icon>attach_money</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                        <v-list-item-title>Total Donations </v-list-item-title>
                        <v-list-item-subtitle>{{ this.total_donations }}</v-list-item-subtitle>
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
                    :items="donations"
                    item-key="donor_id"
                    class="elevation-1"
                    :items-per-page="25"
                />
            </template>
        </v-content>

        <Uploader :upload-dialog.sync="uploadDialog" @close-dialog="uploadDialog = false" />
    </v-app>
</template>

<script>
import Uploader from "./components/Uploader"

export default {
    name: "App",
    components: {
        Uploader
    },
    data: () => ({
        drawer: false,
        uploadDialog: false,
        search: "",
        total_donations: 0,
        donations: [],
        headers: [
            {
                text: "Donor ID",
                align: "left",
                sortable: false,
                value: "donor_id"
            },
            { text: "Name", value: "donor_name" },
            { text: "Email", value: "donor_email" },
            { text: "Gender", value: "donor_gender" },
            { text: "Address", value: "donor_address" },
            { text: "Donation Amount", value: "donation_amount" }
        ]
    }),
    created() {
        this.$chadevmonster_api
            .get("articles")
            .then(async response => {
                response.data.forEach(element => {
                    console.log("element:", element)
                })
            })
            .catch(error => {
                console.log("error", error)
            })
    }
}
</script>
