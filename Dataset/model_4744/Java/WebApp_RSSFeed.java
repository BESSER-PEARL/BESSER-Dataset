





import java.util.List;
import java.util.ArrayList;

public class WebApp_RSSFeed extends ExternalSource {

    private String show_date;
    private String url;
    private String feedname;
    private int items_to_display;



    public WebApp_RSSFeed(
        String show_date,        String url,        String feedname,        int items_to_display    ) {
        super(
        );
        this.show_date = show_date;
        this.url = url;
        this.feedname = feedname;
        this.items_to_display = items_to_display;
    }


    public String getShow_date() {
        return show_date;
    }

    public void setShow_date(String show_date) {
        this.show_date = show_date;
    }
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }
    public String getFeedname() {
        return feedname;
    }

    public void setFeedname(String feedname) {
        this.feedname = feedname;
    }
    public int getItems_to_display() {
        return items_to_display;
    }

    public void setItems_to_display(int items_to_display) {
        this.items_to_display = items_to_display;
    }


}