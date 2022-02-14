declare namespace api {
    /* Example */
    export namespace example {
        interface UserInfo {
            user_id: string;
            fullname: string;
            is_ehr: string;
            person_type: number;
            is_same_device: boolean;
            email: string;
            extra_user_info: {
                user_id: string;
                fullname: string;
                email: string;
            };
        }
    }
}
