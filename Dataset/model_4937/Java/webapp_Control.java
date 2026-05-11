





import java.util.List;
import java.util.ArrayList;

public class webapp_Control  {

    private String id;
    private String name;





    private webapp_FormPage webapp_formpage;


    public webapp_Control(
        String id,        String name    ) {
        this.id = id;
        this.name = name;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public webapp_FormPage getWebapp_formpage() {
        return webapp_formpage;
    }

    public void setWebapp_formpage(webapp_FormPage webapp_formpage) {
        this.webapp_formpage = webapp_formpage;
    }

}