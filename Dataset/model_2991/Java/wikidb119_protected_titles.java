





import java.util.List;
import java.util.ArrayList;

public class wikidb119_protected_titles  {

    private String pt_user;
    private String pt_timestamp;
    private String pt_reason;
    private String pt_namespace;
    private String pt_title;
    private String pt_create_perm;
    private String pt_expiry;



    public wikidb119_protected_titles(
        String pt_user,        String pt_timestamp,        String pt_reason,        String pt_namespace,        String pt_title,        String pt_create_perm,        String pt_expiry    ) {
        this.pt_user = pt_user;
        this.pt_timestamp = pt_timestamp;
        this.pt_reason = pt_reason;
        this.pt_namespace = pt_namespace;
        this.pt_title = pt_title;
        this.pt_create_perm = pt_create_perm;
        this.pt_expiry = pt_expiry;
    }


    public String getPt_user() {
        return pt_user;
    }

    public void setPt_user(String pt_user) {
        this.pt_user = pt_user;
    }
    public String getPt_timestamp() {
        return pt_timestamp;
    }

    public void setPt_timestamp(String pt_timestamp) {
        this.pt_timestamp = pt_timestamp;
    }
    public String getPt_reason() {
        return pt_reason;
    }

    public void setPt_reason(String pt_reason) {
        this.pt_reason = pt_reason;
    }
    public String getPt_namespace() {
        return pt_namespace;
    }

    public void setPt_namespace(String pt_namespace) {
        this.pt_namespace = pt_namespace;
    }
    public String getPt_title() {
        return pt_title;
    }

    public void setPt_title(String pt_title) {
        this.pt_title = pt_title;
    }
    public String getPt_create_perm() {
        return pt_create_perm;
    }

    public void setPt_create_perm(String pt_create_perm) {
        this.pt_create_perm = pt_create_perm;
    }
    public String getPt_expiry() {
        return pt_expiry;
    }

    public void setPt_expiry(String pt_expiry) {
        this.pt_expiry = pt_expiry;
    }


}