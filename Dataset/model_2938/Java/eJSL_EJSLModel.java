





import java.util.List;
import java.util.ArrayList;

public class eJSL_EJSLModel  {

    private String name;





    private eJSL_EJSLPart ejsl_ejslpart;


    public eJSL_EJSLModel(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public eJSL_EJSLPart getEjsl_ejslpart() {
        return ejsl_ejslpart;
    }

    public void setEjsl_ejslpart(eJSL_EJSLPart ejsl_ejslpart) {
        this.ejsl_ejslpart = ejsl_ejslpart;
    }

}