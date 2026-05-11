





import java.util.List;
import java.util.ArrayList;

public class xpdl1_DataFieldType  {

    private String initialValue;
    private String length;
    private String id;
    private String description;
    private String name;
    private String isArray;





    private xpdl1_DataFieldsType xpdl1_datafieldstype;




    private xpdl1_ExtendedAttributesType xpdl1_extendedattributestype;


    public xpdl1_DataFieldType(
        String initialValue,        String length,        String id,        String description,        String name,        String isArray    ) {
        this.initialValue = initialValue;
        this.length = length;
        this.id = id;
        this.description = description;
        this.name = name;
        this.isArray = isArray;
    }


    public String getInitialvalue() {
        return initialValue;
    }

    public void setInitialvalue(String initialValue) {
        this.initialValue = initialValue;
    }
    public String getLength() {
        return length;
    }

    public void setLength(String length) {
        this.length = length;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getIsarray() {
        return isArray;
    }

    public void setIsarray(String isArray) {
        this.isArray = isArray;
    }

    public xpdl1_DataFieldsType getXpdl1_datafieldstype() {
        return xpdl1_datafieldstype;
    }

    public void setXpdl1_datafieldstype(xpdl1_DataFieldsType xpdl1_datafieldstype) {
        this.xpdl1_datafieldstype = xpdl1_datafieldstype;
    }
    public xpdl1_ExtendedAttributesType getXpdl1_extendedattributestype() {
        return xpdl1_extendedattributestype;
    }

    public void setXpdl1_extendedattributestype(xpdl1_ExtendedAttributesType xpdl1_extendedattributestype) {
        this.xpdl1_extendedattributestype = xpdl1_extendedattributestype;
    }

}