





import java.util.List;
import java.util.ArrayList;

public class xpdl1_ExtendedAttributeType  {

    private String mixed;
    private String group;
    private String value;
    private String name;
    private String any;





    private xpdl1_DocumentRoot xpdl1_documentroot;




    private xpdl1_ExtendedAttributesType xpdl1_extendedattributestype;


    public xpdl1_ExtendedAttributeType(
        String mixed,        String group,        String value,        String name,        String any    ) {
        this.mixed = mixed;
        this.group = group;
        this.value = value;
        this.name = name;
        this.any = any;
    }


    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAny() {
        return any;
    }

    public void setAny(String any) {
        this.any = any;
    }

    public xpdl1_DocumentRoot getXpdl1_documentroot() {
        return xpdl1_documentroot;
    }

    public void setXpdl1_documentroot(xpdl1_DocumentRoot xpdl1_documentroot) {
        this.xpdl1_documentroot = xpdl1_documentroot;
    }
    public xpdl1_ExtendedAttributesType getXpdl1_extendedattributestype() {
        return xpdl1_extendedattributestype;
    }

    public void setXpdl1_extendedattributestype(xpdl1_ExtendedAttributesType xpdl1_extendedattributestype) {
        this.xpdl1_extendedattributestype = xpdl1_extendedattributestype;
    }

}