





import java.util.List;
import java.util.ArrayList;

public class eJSL_MethodParameter  {

    private String name;





    private eJSL_Type ejsl_type;




    private eJSL_Method ejsl_method;


    public eJSL_MethodParameter(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public eJSL_Type getEjsl_type() {
        return ejsl_type;
    }

    public void setEjsl_type(eJSL_Type ejsl_type) {
        this.ejsl_type = ejsl_type;
    }
    public eJSL_Method getEjsl_method() {
        return ejsl_method;
    }

    public void setEjsl_method(eJSL_Method ejsl_method) {
        this.ejsl_method = ejsl_method;
    }

}