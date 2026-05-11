





import java.util.List;
import java.util.ArrayList;

public class wikidb116_page_restrictions  {

    private String pr_page;
    private String pr_expiry;
    private int pr_cascade;
    private String pr_user;
    private String pr_type;
    private String pr_id;
    private String pr_level;



    public wikidb116_page_restrictions(
        String pr_page,        String pr_expiry,        int pr_cascade,        String pr_user,        String pr_type,        String pr_id,        String pr_level    ) {
        this.pr_page = pr_page;
        this.pr_expiry = pr_expiry;
        this.pr_cascade = pr_cascade;
        this.pr_user = pr_user;
        this.pr_type = pr_type;
        this.pr_id = pr_id;
        this.pr_level = pr_level;
    }


    public String getPr_page() {
        return pr_page;
    }

    public void setPr_page(String pr_page) {
        this.pr_page = pr_page;
    }
    public String getPr_expiry() {
        return pr_expiry;
    }

    public void setPr_expiry(String pr_expiry) {
        this.pr_expiry = pr_expiry;
    }
    public int getPr_cascade() {
        return pr_cascade;
    }

    public void setPr_cascade(int pr_cascade) {
        this.pr_cascade = pr_cascade;
    }
    public String getPr_user() {
        return pr_user;
    }

    public void setPr_user(String pr_user) {
        this.pr_user = pr_user;
    }
    public String getPr_type() {
        return pr_type;
    }

    public void setPr_type(String pr_type) {
        this.pr_type = pr_type;
    }
    public String getPr_id() {
        return pr_id;
    }

    public void setPr_id(String pr_id) {
        this.pr_id = pr_id;
    }
    public String getPr_level() {
        return pr_level;
    }

    public void setPr_level(String pr_level) {
        this.pr_level = pr_level;
    }


}