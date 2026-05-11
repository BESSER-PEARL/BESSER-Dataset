





import java.util.List;
import java.util.ArrayList;

public class camel_Action  {

    private String type;
    private String name;





    private camel_CamelModel camel_camelmodel;


    public camel_Action(
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

    public camel_CamelModel getCamel_camelmodel() {
        return camel_camelmodel;
    }

    public void setCamel_camelmodel(camel_CamelModel camel_camelmodel) {
        this.camel_camelmodel = camel_camelmodel;
    }

}