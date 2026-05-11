





import java.util.List;
import java.util.ArrayList;

public class xhtml_ParamType  {

    private String id;
    private String name;
    private String type;
    private String value;
    private String valuetype;





    private xhtml_DocumentRoot xhtml_documentroot;




    private xhtml_ObjectType xhtml_objecttype;


    public xhtml_ParamType(
        String id,        String name,        String type,        String value,        String valuetype    ) {
        this.id = id;
        this.name = name;
        this.type = type;
        this.value = value;
        this.valuetype = valuetype;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public String getValuetype() {
        return valuetype;
    }

    public void setValuetype(String valuetype) {
        this.valuetype = valuetype;
    }

    public xhtml_DocumentRoot getXhtml_documentroot() {
        return xhtml_documentroot;
    }

    public void setXhtml_documentroot(xhtml_DocumentRoot xhtml_documentroot) {
        this.xhtml_documentroot = xhtml_documentroot;
    }
    public xhtml_ObjectType getXhtml_objecttype() {
        return xhtml_objecttype;
    }

    public void setXhtml_objecttype(xhtml_ObjectType xhtml_objecttype) {
        this.xhtml_objecttype = xhtml_objecttype;
    }

}