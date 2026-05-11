





import java.util.List;
import java.util.ArrayList;

public class eJSL_Position  {

    private String name;





    private eJSL_Template ejsl_template;


    public eJSL_Position(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public eJSL_Template getEjsl_template() {
        return ejsl_template;
    }

    public void setEjsl_template(eJSL_Template ejsl_template) {
        this.ejsl_template = ejsl_template;
    }

}