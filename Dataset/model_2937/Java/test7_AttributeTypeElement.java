





import java.util.List;
import java.util.ArrayList;

public class test7_AttributeTypeElement  {

    private String name;
    private String dataType;





    private test7_AttributeType test7_attributetype;


    public test7_AttributeTypeElement(
        String name,        String dataType    ) {
        this.name = name;
        this.dataType = dataType;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDatatype() {
        return dataType;
    }

    public void setDatatype(String dataType) {
        this.dataType = dataType;
    }

    public test7_AttributeType getTest7_attributetype() {
        return test7_attributetype;
    }

    public void setTest7_attributetype(test7_AttributeType test7_attributetype) {
        this.test7_attributetype = test7_attributetype;
    }

}