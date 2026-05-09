





import java.util.List;
import java.util.ArrayList;

public class mvc_View  {

    private String type;
    private String name;





    private mvc_MvcApplication mvc_mvcapplication;


    public mvc_View(
        String type,        String name    ) {
        this.type = type;
        this.name = name;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public mvc_MvcApplication getMvc_mvcapplication() {
        return mvc_mvcapplication;
    }

    public void setMvc_mvcapplication(mvc_MvcApplication mvc_mvcapplication) {
        this.mvc_mvcapplication = mvc_mvcapplication;
    }

}