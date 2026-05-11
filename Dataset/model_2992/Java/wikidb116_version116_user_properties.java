





import java.util.List;
import java.util.ArrayList;

public class wikidb116_version116_user_properties  {

    private String up_user;
    private String up_value;
    private String up_property;



    public wikidb116_version116_user_properties(
        String up_user,        String up_value,        String up_property    ) {
        this.up_user = up_user;
        this.up_value = up_value;
        this.up_property = up_property;
    }


    public String getUp_user() {
        return up_user;
    }

    public void setUp_user(String up_user) {
        this.up_user = up_user;
    }
    public String getUp_value() {
        return up_value;
    }

    public void setUp_value(String up_value) {
        this.up_value = up_value;
    }
    public String getUp_property() {
        return up_property;
    }

    public void setUp_property(String up_property) {
        this.up_property = up_property;
    }


}