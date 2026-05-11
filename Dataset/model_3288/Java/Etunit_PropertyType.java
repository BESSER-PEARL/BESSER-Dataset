





import java.util.List;
import java.util.ArrayList;

public class Etunit_PropertyType  {

    private String name;
    private String value;





    private Etunit_PropertiesType etunit_propertiestype;




    private Etunit_DocumentRoot etunit_documentroot;


    public Etunit_PropertyType(
        String name,        String value    ) {
        this.name = name;
        this.value = value;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public Etunit_PropertiesType getEtunit_propertiestype() {
        return etunit_propertiestype;
    }

    public void setEtunit_propertiestype(Etunit_PropertiesType etunit_propertiestype) {
        this.etunit_propertiestype = etunit_propertiestype;
    }
    public Etunit_DocumentRoot getEtunit_documentroot() {
        return etunit_documentroot;
    }

    public void setEtunit_documentroot(Etunit_DocumentRoot etunit_documentroot) {
        this.etunit_documentroot = etunit_documentroot;
    }

}