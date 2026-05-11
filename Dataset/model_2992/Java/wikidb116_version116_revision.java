





import java.util.List;
import java.util.ArrayList;

public class wikidb116_version116_revision  {

    private int rev_deleted;
    private int rev_minor_edit;
    private String rev_comment;
    private String rev_id;
    private String rev_len;
    private String rev_user;
    private String rev_parent_id;
    private String rev_text_id;
    private String rev_user_text;
    private String rev_page;
    private String rev_timestamp;



    public wikidb116_version116_revision(
        int rev_deleted,        int rev_minor_edit,        String rev_comment,        String rev_id,        String rev_len,        String rev_user,        String rev_parent_id,        String rev_text_id,        String rev_user_text,        String rev_page,        String rev_timestamp    ) {
        this.rev_deleted = rev_deleted;
        this.rev_minor_edit = rev_minor_edit;
        this.rev_comment = rev_comment;
        this.rev_id = rev_id;
        this.rev_len = rev_len;
        this.rev_user = rev_user;
        this.rev_parent_id = rev_parent_id;
        this.rev_text_id = rev_text_id;
        this.rev_user_text = rev_user_text;
        this.rev_page = rev_page;
        this.rev_timestamp = rev_timestamp;
    }


    public int getRev_deleted() {
        return rev_deleted;
    }

    public void setRev_deleted(int rev_deleted) {
        this.rev_deleted = rev_deleted;
    }
    public int getRev_minor_edit() {
        return rev_minor_edit;
    }

    public void setRev_minor_edit(int rev_minor_edit) {
        this.rev_minor_edit = rev_minor_edit;
    }
    public String getRev_comment() {
        return rev_comment;
    }

    public void setRev_comment(String rev_comment) {
        this.rev_comment = rev_comment;
    }
    public String getRev_id() {
        return rev_id;
    }

    public void setRev_id(String rev_id) {
        this.rev_id = rev_id;
    }
    public String getRev_len() {
        return rev_len;
    }

    public void setRev_len(String rev_len) {
        this.rev_len = rev_len;
    }
    public String getRev_user() {
        return rev_user;
    }

    public void setRev_user(String rev_user) {
        this.rev_user = rev_user;
    }
    public String getRev_parent_id() {
        return rev_parent_id;
    }

    public void setRev_parent_id(String rev_parent_id) {
        this.rev_parent_id = rev_parent_id;
    }
    public String getRev_text_id() {
        return rev_text_id;
    }

    public void setRev_text_id(String rev_text_id) {
        this.rev_text_id = rev_text_id;
    }
    public String getRev_user_text() {
        return rev_user_text;
    }

    public void setRev_user_text(String rev_user_text) {
        this.rev_user_text = rev_user_text;
    }
    public String getRev_page() {
        return rev_page;
    }

    public void setRev_page(String rev_page) {
        this.rev_page = rev_page;
    }
    public String getRev_timestamp() {
        return rev_timestamp;
    }

    public void setRev_timestamp(String rev_timestamp) {
        this.rev_timestamp = rev_timestamp;
    }


}