





import java.util.List;
import java.util.ArrayList;

public class wikidb119_user_groups  {

    private String ug_group;
    private String ug_user;



    public wikidb119_user_groups(
        String ug_group,        String ug_user    ) {
        this.ug_group = ug_group;
        this.ug_user = ug_user;
    }


    public String getUg_group() {
        return ug_group;
    }

    public void setUg_group(String ug_group) {
        this.ug_group = ug_group;
    }
    public String getUg_user() {
        return ug_user;
    }

    public void setUg_user(String ug_user) {
        this.ug_user = ug_user;
    }


}