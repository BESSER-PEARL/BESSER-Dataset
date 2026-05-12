





import java.util.List;
import java.util.ArrayList;

public class xwiki_Property extends LinkCollection {

    private String type;
    private String value;
    private String name;





    private xwiki_PropertiesType xwiki_propertiestype;




    private xwiki_Class xwiki_class;




    private List<xwiki_Attribute> xwiki_attributes;


    public xwiki_Property(
        String type,        String value,        String name    ) {
        super(
        );
        this.type = type;
        this.value = value;
        this.name = name;
        this.xwiki_attributes = new ArrayList<>();
    }

    public xwiki_Property(
        String type,        String value,        String name        ArrayList<xwiki_Attribute> xwiki_attributes    ) {
        this.type = type;
        this.value = value;
        this.name = name;
        this.xwiki_attributes = xwiki_attributes;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
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

    public xwiki_PropertiesType getXwiki_propertiestype() {
        return xwiki_propertiestype;
    }

    public void setXwiki_propertiestype(xwiki_PropertiesType xwiki_propertiestype) {
        this.xwiki_propertiestype = xwiki_propertiestype;
    }
    public xwiki_Class getXwiki_class() {
        return xwiki_class;
    }

    public void setXwiki_class(xwiki_Class xwiki_class) {
        this.xwiki_class = xwiki_class;
    }
    public List<xwiki_Attribute> getXwiki_attributes() {
        return xwiki_attributes;
    }

    public void addXwiki_attribute(Xwiki_attribute xwiki_attribute) {
        this.xwiki_attributes.add(xwiki_attribute);
    }

}