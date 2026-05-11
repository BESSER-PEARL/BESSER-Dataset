





import java.util.List;
import java.util.ArrayList;

public class carnot_AttributeType  {

    private String any;
    private String mixed;
    private String value;
    private String name;
    private String group;
    private String type;





    private carnot_IExtensibleElement carnot_iextensibleelement;


    public carnot_AttributeType(
        String any,        String mixed,        String value,        String name,        String group,        String type    ) {
        this.any = any;
        this.mixed = mixed;
        this.value = value;
        this.name = name;
        this.group = group;
        this.type = type;
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
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public carnot_IExtensibleElement getCarnot_iextensibleelement() {
        return carnot_iextensibleelement;
    }

    public void setCarnot_iextensibleelement(carnot_IExtensibleElement carnot_iextensibleelement) {
        this.carnot_iextensibleelement = carnot_iextensibleelement;
    }

}