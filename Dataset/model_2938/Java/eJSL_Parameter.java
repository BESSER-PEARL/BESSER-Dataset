





import java.util.List;
import java.util.ArrayList;

public class eJSL_Parameter  {

    private String name;
    private String label;
    private int size;
    private String defaultvalue;
    private String descripton;





    private eJSL_EJSLPart ejsl_ejslpart;


    public eJSL_Parameter(
        String name,        String label,        int size,        String defaultvalue,        String descripton    ) {
        this.name = name;
        this.label = label;
        this.size = size;
        this.defaultvalue = defaultvalue;
        this.descripton = descripton;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }
    public String getDefaultvalue() {
        return defaultvalue;
    }

    public void setDefaultvalue(String defaultvalue) {
        this.defaultvalue = defaultvalue;
    }
    public String getDescripton() {
        return descripton;
    }

    public void setDescripton(String descripton) {
        this.descripton = descripton;
    }

    public eJSL_EJSLPart getEjsl_ejslpart() {
        return ejsl_ejslpart;
    }

    public void setEjsl_ejslpart(eJSL_EJSLPart ejsl_ejslpart) {
        this.ejsl_ejslpart = ejsl_ejslpart;
    }

}