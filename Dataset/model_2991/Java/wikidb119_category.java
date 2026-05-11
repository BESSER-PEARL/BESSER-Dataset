





import java.util.List;
import java.util.ArrayList;

public class wikidb119_category  {

    private String cat_id;
    private String cat_title;
    private String cat_pages;
    private String cat_files;
    private int cat_hidden;
    private String cat_subcats;



    public wikidb119_category(
        String cat_id,        String cat_title,        String cat_pages,        String cat_files,        int cat_hidden,        String cat_subcats    ) {
        this.cat_id = cat_id;
        this.cat_title = cat_title;
        this.cat_pages = cat_pages;
        this.cat_files = cat_files;
        this.cat_hidden = cat_hidden;
        this.cat_subcats = cat_subcats;
    }


    public String getCat_id() {
        return cat_id;
    }

    public void setCat_id(String cat_id) {
        this.cat_id = cat_id;
    }
    public String getCat_title() {
        return cat_title;
    }

    public void setCat_title(String cat_title) {
        this.cat_title = cat_title;
    }
    public String getCat_pages() {
        return cat_pages;
    }

    public void setCat_pages(String cat_pages) {
        this.cat_pages = cat_pages;
    }
    public String getCat_files() {
        return cat_files;
    }

    public void setCat_files(String cat_files) {
        this.cat_files = cat_files;
    }
    public int getCat_hidden() {
        return cat_hidden;
    }

    public void setCat_hidden(int cat_hidden) {
        this.cat_hidden = cat_hidden;
    }
    public String getCat_subcats() {
        return cat_subcats;
    }

    public void setCat_subcats(String cat_subcats) {
        this.cat_subcats = cat_subcats;
    }


}