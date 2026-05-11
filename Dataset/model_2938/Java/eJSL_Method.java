





import java.util.List;
import java.util.ArrayList;

public class eJSL_Method  {

    private String name;
    private String returnvalue;





    private eJSL_Type ejsl_type;




    private eJSL_Class ejsl_class;


    public eJSL_Method(
        String name,        String returnvalue    ) {
        this.name = name;
        this.returnvalue = returnvalue;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getReturnvalue() {
        return returnvalue;
    }

    public void setReturnvalue(String returnvalue) {
        this.returnvalue = returnvalue;
    }

    public eJSL_Type getEjsl_type() {
        return ejsl_type;
    }

    public void setEjsl_type(eJSL_Type ejsl_type) {
        this.ejsl_type = ejsl_type;
    }
    public eJSL_Class getEjsl_class() {
        return ejsl_class;
    }

    public void setEjsl_class(eJSL_Class ejsl_class) {
        this.ejsl_class = ejsl_class;
    }

}