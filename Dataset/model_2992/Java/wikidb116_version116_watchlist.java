





import java.util.List;
import java.util.ArrayList;

public class wikidb116_version116_watchlist  {

    private String wl_user;
    private String wl_notificationtimestamp;
    private String wl_title;
    private String wl_namespace;



    public wikidb116_version116_watchlist(
        String wl_user,        String wl_notificationtimestamp,        String wl_title,        String wl_namespace    ) {
        this.wl_user = wl_user;
        this.wl_notificationtimestamp = wl_notificationtimestamp;
        this.wl_title = wl_title;
        this.wl_namespace = wl_namespace;
    }


    public String getWl_user() {
        return wl_user;
    }

    public void setWl_user(String wl_user) {
        this.wl_user = wl_user;
    }
    public String getWl_notificationtimestamp() {
        return wl_notificationtimestamp;
    }

    public void setWl_notificationtimestamp(String wl_notificationtimestamp) {
        this.wl_notificationtimestamp = wl_notificationtimestamp;
    }
    public String getWl_title() {
        return wl_title;
    }

    public void setWl_title(String wl_title) {
        this.wl_title = wl_title;
    }
    public String getWl_namespace() {
        return wl_namespace;
    }

    public void setWl_namespace(String wl_namespace) {
        this.wl_namespace = wl_namespace;
    }


}