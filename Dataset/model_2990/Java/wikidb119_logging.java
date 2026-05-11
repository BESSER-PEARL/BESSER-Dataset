





import java.util.List;
import java.util.ArrayList;

public class wikidb119_logging  {

    private String log_params;
    private String log_timestamp;
    private String log_id;
    private String log_namespace;
    private String log_type;
    private int log_deleted;
    private String log_title;
    private String log_action;
    private String log_comment;
    private String log_user;
    private String log_user_text;
    private String log_page;



    public wikidb119_logging(
        String log_params,        String log_timestamp,        String log_id,        String log_namespace,        String log_type,        int log_deleted,        String log_title,        String log_action,        String log_comment,        String log_user,        String log_user_text,        String log_page    ) {
        this.log_params = log_params;
        this.log_timestamp = log_timestamp;
        this.log_id = log_id;
        this.log_namespace = log_namespace;
        this.log_type = log_type;
        this.log_deleted = log_deleted;
        this.log_title = log_title;
        this.log_action = log_action;
        this.log_comment = log_comment;
        this.log_user = log_user;
        this.log_user_text = log_user_text;
        this.log_page = log_page;
    }


    public String getLog_params() {
        return log_params;
    }

    public void setLog_params(String log_params) {
        this.log_params = log_params;
    }
    public String getLog_timestamp() {
        return log_timestamp;
    }

    public void setLog_timestamp(String log_timestamp) {
        this.log_timestamp = log_timestamp;
    }
    public String getLog_id() {
        return log_id;
    }

    public void setLog_id(String log_id) {
        this.log_id = log_id;
    }
    public String getLog_namespace() {
        return log_namespace;
    }

    public void setLog_namespace(String log_namespace) {
        this.log_namespace = log_namespace;
    }
    public String getLog_type() {
        return log_type;
    }

    public void setLog_type(String log_type) {
        this.log_type = log_type;
    }
    public int getLog_deleted() {
        return log_deleted;
    }

    public void setLog_deleted(int log_deleted) {
        this.log_deleted = log_deleted;
    }
    public String getLog_title() {
        return log_title;
    }

    public void setLog_title(String log_title) {
        this.log_title = log_title;
    }
    public String getLog_action() {
        return log_action;
    }

    public void setLog_action(String log_action) {
        this.log_action = log_action;
    }
    public String getLog_comment() {
        return log_comment;
    }

    public void setLog_comment(String log_comment) {
        this.log_comment = log_comment;
    }
    public String getLog_user() {
        return log_user;
    }

    public void setLog_user(String log_user) {
        this.log_user = log_user;
    }
    public String getLog_user_text() {
        return log_user_text;
    }

    public void setLog_user_text(String log_user_text) {
        this.log_user_text = log_user_text;
    }
    public String getLog_page() {
        return log_page;
    }

    public void setLog_page(String log_page) {
        this.log_page = log_page;
    }


}