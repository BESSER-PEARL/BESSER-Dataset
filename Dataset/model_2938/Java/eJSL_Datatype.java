





import java.util.List;
import java.util.ArrayList;

public class eJSL_Datatype  {

    private String name;
    private String type;





    private eJSL_EJSLPart ejsl_ejslpart;


    public eJSL_Datatype(
        String name,        String type    ) {
        this.name = name;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public eJSL_EJSLPart getEjsl_ejslpart() {
        return ejsl_ejslpart;
    }

    public void setEjsl_ejslpart(eJSL_EJSLPart ejsl_ejslpart) {
        this.ejsl_ejslpart = ejsl_ejslpart;
    }

}