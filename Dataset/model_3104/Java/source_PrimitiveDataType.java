





import java.util.List;
import java.util.ArrayList;

public class source_PrimitiveDataType  {

    private String name;





    private source_Attribute source_attribute;


    public source_PrimitiveDataType(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public source_Attribute getSource_attribute() {
        return source_attribute;
    }

    public void setSource_attribute(source_Attribute source_attribute) {
        this.source_attribute = source_attribute;
    }

}