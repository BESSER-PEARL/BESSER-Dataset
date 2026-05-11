





import java.util.List;
import java.util.ArrayList;

public class wikidb119_searchindex  {

    private String si_text;
    private String si_page;
    private String si_title;



    public wikidb119_searchindex(
        String si_text,        String si_page,        String si_title    ) {
        this.si_text = si_text;
        this.si_page = si_page;
        this.si_title = si_title;
    }


    public String getSi_text() {
        return si_text;
    }

    public void setSi_text(String si_text) {
        this.si_text = si_text;
    }
    public String getSi_page() {
        return si_page;
    }

    public void setSi_page(String si_page) {
        this.si_page = si_page;
    }
    public String getSi_title() {
        return si_title;
    }

    public void setSi_title(String si_title) {
        this.si_title = si_title;
    }


}