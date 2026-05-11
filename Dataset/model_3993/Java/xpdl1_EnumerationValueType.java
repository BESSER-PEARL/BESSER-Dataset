





import java.util.List;
import java.util.ArrayList;

public class xpdl1_EnumerationValueType  {

    private String name;





    private xpdl1_DocumentRoot xpdl1_documentroot;




    private xpdl1_EnumerationTypeType xpdl1_enumerationtypetype;


    public xpdl1_EnumerationValueType(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public xpdl1_DocumentRoot getXpdl1_documentroot() {
        return xpdl1_documentroot;
    }

    public void setXpdl1_documentroot(xpdl1_DocumentRoot xpdl1_documentroot) {
        this.xpdl1_documentroot = xpdl1_documentroot;
    }
    public xpdl1_EnumerationTypeType getXpdl1_enumerationtypetype() {
        return xpdl1_enumerationtypetype;
    }

    public void setXpdl1_enumerationtypetype(xpdl1_EnumerationTypeType xpdl1_enumerationtypetype) {
        this.xpdl1_enumerationtypetype = xpdl1_enumerationtypetype;
    }

}