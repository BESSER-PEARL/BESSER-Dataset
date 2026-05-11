





import java.util.List;
import java.util.ArrayList;

public class swml_Entity  {

    private String name;





    private swml_WebApplication swml_webapplication;


    public swml_Entity(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public swml_WebApplication getSwml_webapplication() {
        return swml_webapplication;
    }

    public void setSwml_webapplication(swml_WebApplication swml_webapplication) {
        this.swml_webapplication = swml_webapplication;
    }

}