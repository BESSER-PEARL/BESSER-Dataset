





import java.util.List;
import java.util.ArrayList;

public class xpdl2_ExtendedAttributeType  {

    private String value;
    private String name;
    private String group;
    private String any;
    private String mixed;





    private xpdl2_ExtendedAttributesType xpdl2_extendedattributestype;


    public xpdl2_ExtendedAttributeType(
        String value,        String name,        String group,        String any,        String mixed    ) {
        this.value = value;
        this.name = name;
        this.group = group;
        this.any = any;
        this.mixed = mixed;
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
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getAny() {
        return any;
    }

    public void setAny(String any) {
        this.any = any;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public xpdl2_ExtendedAttributesType getXpdl2_extendedattributestype() {
        return xpdl2_extendedattributestype;
    }

    public void setXpdl2_extendedattributestype(xpdl2_ExtendedAttributesType xpdl2_extendedattributestype) {
        this.xpdl2_extendedattributestype = xpdl2_extendedattributestype;
    }

}