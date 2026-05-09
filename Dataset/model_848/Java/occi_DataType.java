





import java.util.List;
import java.util.ArrayList;

public class occi_DataType  {

    private String name;
    private String documentation;





    private occi_Attribute occi_attribute;


    public occi_DataType(
        String name,        String documentation    ) {
        this.name = name;
        this.documentation = documentation;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDocumentation() {
        return documentation;
    }

    public void setDocumentation(String documentation) {
        this.documentation = documentation;
    }

    public occi_Attribute getOcci_attribute() {
        return occi_attribute;
    }

    public void setOcci_attribute(occi_Attribute occi_attribute) {
        this.occi_attribute = occi_attribute;
    }

}