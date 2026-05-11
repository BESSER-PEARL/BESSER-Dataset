





import java.util.List;
import java.util.ArrayList;

public class wikidb119_site_stats  {

    private String ss_users;
    private String ss_total_pages;
    private String ss_total_views;
    private String ss_admins;
    private String ss_images;
    private String ss_good_articles;
    private String ss_row_id;
    private String ss_active_users;
    private String ss_total_edits;



    public wikidb119_site_stats(
        String ss_users,        String ss_total_pages,        String ss_total_views,        String ss_admins,        String ss_images,        String ss_good_articles,        String ss_row_id,        String ss_active_users,        String ss_total_edits    ) {
        this.ss_users = ss_users;
        this.ss_total_pages = ss_total_pages;
        this.ss_total_views = ss_total_views;
        this.ss_admins = ss_admins;
        this.ss_images = ss_images;
        this.ss_good_articles = ss_good_articles;
        this.ss_row_id = ss_row_id;
        this.ss_active_users = ss_active_users;
        this.ss_total_edits = ss_total_edits;
    }


    public String getSs_users() {
        return ss_users;
    }

    public void setSs_users(String ss_users) {
        this.ss_users = ss_users;
    }
    public String getSs_total_pages() {
        return ss_total_pages;
    }

    public void setSs_total_pages(String ss_total_pages) {
        this.ss_total_pages = ss_total_pages;
    }
    public String getSs_total_views() {
        return ss_total_views;
    }

    public void setSs_total_views(String ss_total_views) {
        this.ss_total_views = ss_total_views;
    }
    public String getSs_admins() {
        return ss_admins;
    }

    public void setSs_admins(String ss_admins) {
        this.ss_admins = ss_admins;
    }
    public String getSs_images() {
        return ss_images;
    }

    public void setSs_images(String ss_images) {
        this.ss_images = ss_images;
    }
    public String getSs_good_articles() {
        return ss_good_articles;
    }

    public void setSs_good_articles(String ss_good_articles) {
        this.ss_good_articles = ss_good_articles;
    }
    public String getSs_row_id() {
        return ss_row_id;
    }

    public void setSs_row_id(String ss_row_id) {
        this.ss_row_id = ss_row_id;
    }
    public String getSs_active_users() {
        return ss_active_users;
    }

    public void setSs_active_users(String ss_active_users) {
        this.ss_active_users = ss_active_users;
    }
    public String getSs_total_edits() {
        return ss_total_edits;
    }

    public void setSs_total_edits(String ss_total_edits) {
        this.ss_total_edits = ss_total_edits;
    }


}