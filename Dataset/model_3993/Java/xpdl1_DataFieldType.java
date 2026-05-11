





import java.util.List;
import java.util.ArrayList;

public class xpdl1_DataFieldType  {

    private String initialValue;
    private String name;
    private String isArray;
    private String description;
    private String length;
    private String id;





    private xpdl1_ExtendedAttributesType xpdl1_extendedattributestype;




    private xpdl1_DataFieldsType xpdl1_datafieldstype;


    public xpdl1_DataFieldType(
        String initialValue,        String name,        String isArray,        String description,        String length,        String id    ) {
        this.initialValue = initialValue;
        this.name = name;
        this.isArray = isArray;
        this.description = description;
        this.length = length;
        this.id = id;
    }


    public String getInitialvalue() {
        return initialValue;
    }

    public void setInitialvalue(String initialValue) {
        this.initialValue = initialValue;
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
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
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

    public xpdl1_ExtendedAttributesType getXpdl1_extendedattributestype() {
        return xpdl1_extendedattributestype;
    }

    public void setXpdl1_extendedattributestype(xpdl1_ExtendedAttributesType xpdl1_extendedattributestype) {
        this.xpdl1_extendedattributestype = xpdl1_extendedattributestype;
    }
    public xpdl1_DataFieldsType getXpdl1_datafieldstype() {
        return xpdl1_datafieldstype;
    }

    public void setXpdl1_datafieldstype(xpdl1_DataFieldsType xpdl1_datafieldstype) {
        this.xpdl1_datafieldstype = xpdl1_datafieldstype;
    }

}