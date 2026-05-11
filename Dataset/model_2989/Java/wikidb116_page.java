





import java.util.List;
import java.util.ArrayList;

public class wikidb116_page  {

    private String page_restrictions;
    private String page_len;
    private String page_title;
    private String page_counter;
    private int page_is_redirect;
    private String page_namespace;
    private float page_random;
    private String page_touched;
    private String page_id;
    private String page_latest;
    private int page_is_new;



    public wikidb116_page(
        String page_restrictions,        String page_len,        String page_title,        String page_counter,        int page_is_redirect,        String page_namespace,        float page_random,        String page_touched,        String page_id,        String page_latest,        int page_is_new    ) {
        this.page_restrictions = page_restrictions;
        this.page_len = page_len;
        this.page_title = page_title;
        this.page_counter = page_counter;
        this.page_is_redirect = page_is_redirect;
        this.page_namespace = page_namespace;
        this.page_random = page_random;
        this.page_touched = page_touched;
        this.page_id = page_id;
        this.page_latest = page_latest;
        this.page_is_new = page_is_new;
    }


    public String getPage_restrictions() {
        return page_restrictions;
    }

    public void setPage_restrictions(String page_restrictions) {
        this.page_restrictions = page_restrictions;
    }
    public String getPage_len() {
        return page_len;
    }

    public void setPage_len(String page_len) {
        this.page_len = page_len;
    }
    public String getPage_title() {
        return page_title;
    }

    public void setPage_title(String page_title) {
        this.page_title = page_title;
    }
    public String getPage_counter() {
        return page_counter;
    }

    public void setPage_counter(String page_counter) {
        this.page_counter = page_counter;
    }
    public int getPage_is_redirect() {
        return page_is_redirect;
    }

    public void setPage_is_redirect(int page_is_redirect) {
        this.page_is_redirect = page_is_redirect;
    }
    public String getPage_namespace() {
        return page_namespace;
    }

    public void setPage_namespace(String page_namespace) {
        this.page_namespace = page_namespace;
    }
    public float getPage_random() {
        return page_random;
    }

    public void setPage_random(float page_random) {
        this.page_random = page_random;
    }
    public String getPage_touched() {
        return page_touched;
    }

    public void setPage_touched(String page_touched) {
        this.page_touched = page_touched;
    }
    public String getPage_id() {
        return page_id;
    }

    public void setPage_id(String page_id) {
        this.page_id = page_id;
    }
    public String getPage_latest() {
        return page_latest;
    }

    public void setPage_latest(String page_latest) {
        this.page_latest = page_latest;
    }
    public int getPage_is_new() {
        return page_is_new;
    }

    public void setPage_is_new(int page_is_new) {
        this.page_is_new = page_is_new;
    }


}