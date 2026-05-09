





import java.util.List;
import java.util.ArrayList;

public class webapp_OnDelete  {

    private String behavior;





    private webapp_ForeignKey webapp_foreignkey;


    public webapp_OnDelete(
        String behavior    ) {
        this.behavior = behavior;
    }


    public String getBehavior() {
        return behavior;
    }

    public void setBehavior(String behavior) {
        this.behavior = behavior;
    }

    public webapp_ForeignKey getWebapp_foreignkey() {
        return webapp_foreignkey;
    }

    public void setWebapp_foreignkey(webapp_ForeignKey webapp_foreignkey) {
        this.webapp_foreignkey = webapp_foreignkey;
    }

}