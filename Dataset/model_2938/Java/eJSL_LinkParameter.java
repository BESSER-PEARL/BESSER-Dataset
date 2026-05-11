





import java.util.List;
import java.util.ArrayList;

public class eJSL_LinkParameter  {

    private String value;
    private boolean id;
    private String name;





    private eJSL_ContextLink ejsl_contextlink;




    private eJSL_Attribute ejsl_attribute;


    public eJSL_LinkParameter(
        String value,        boolean id,        String name    ) {
        this.value = value;
        this.id = id;
        this.name = name;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public boolean getId() {
        return id;
    }

    public void setId(boolean id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public eJSL_ContextLink getEjsl_contextlink() {
        return ejsl_contextlink;
    }

    public void setEjsl_contextlink(eJSL_ContextLink ejsl_contextlink) {
        this.ejsl_contextlink = ejsl_contextlink;
    }
    public eJSL_Attribute getEjsl_attribute() {
        return ejsl_attribute;
    }

    public void setEjsl_attribute(eJSL_Attribute ejsl_attribute) {
        this.ejsl_attribute = ejsl_attribute;
    }

}