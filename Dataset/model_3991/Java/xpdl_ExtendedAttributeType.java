





import java.util.List;
import java.util.ArrayList;

public class xpdl_ExtendedAttributeType  {

    private String mixed;
    private String name;
    private String value;
    private String any;
    private String group;





    private ExtendedAnnotationType extendedannotationtype;




    private xpdl_ExtendedAttributesType xpdl_extendedattributestype;


    public xpdl_ExtendedAttributeType(
        String mixed,        String name,        String value,        String any,        String group    ) {
        this.mixed = mixed;
        this.name = name;
        this.value = value;
        this.any = any;
        this.group = group;
    }


    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
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
    public String getAny() {
        return any;
    }

    public void setAny(String any) {
        this.any = any;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }

    public ExtendedAnnotationType getExtendedannotationtype() {
        return extendedannotationtype;
    }

    public void setExtendedannotationtype(ExtendedAnnotationType extendedannotationtype) {
        this.extendedannotationtype = extendedannotationtype;
    }
    public xpdl_ExtendedAttributesType getXpdl_extendedattributestype() {
        return xpdl_extendedattributestype;
    }

    public void setXpdl_extendedattributestype(xpdl_ExtendedAttributesType xpdl_extendedattributestype) {
        this.xpdl_extendedattributestype = xpdl_extendedattributestype;
    }

}