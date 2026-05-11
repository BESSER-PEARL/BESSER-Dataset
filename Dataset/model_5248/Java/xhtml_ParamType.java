





import java.util.List;
import java.util.ArrayList;

public class xhtml_ParamType  {

    private String valuetype;
    private String name;
    private String id;
    private String value;
    private String type;





    private xhtml_ObjectType xhtml_objecttype;




    private xhtml_DocumentRoot xhtml_documentroot;


    public xhtml_ParamType(
        String valuetype,        String name,        String id,        String value,        String type    ) {
        this.valuetype = valuetype;
        this.name = name;
        this.id = id;
        this.value = value;
        this.type = type;
    }


    public String getValuetype() {
        return valuetype;
    }

    public void setValuetype(String valuetype) {
        this.valuetype = valuetype;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public xhtml_ObjectType getXhtml_objecttype() {
        return xhtml_objecttype;
    }

    public void setXhtml_objecttype(xhtml_ObjectType xhtml_objecttype) {
        this.xhtml_objecttype = xhtml_objecttype;
    }
    public xhtml_DocumentRoot getXhtml_documentroot() {
        return xhtml_documentroot;
    }

    public void setXhtml_documentroot(xhtml_DocumentRoot xhtml_documentroot) {
        this.xhtml_documentroot = xhtml_documentroot;
    }

}