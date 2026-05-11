





import java.util.List;
import java.util.ArrayList;

public class coCoMM_AttributeTypeElement  {

    private String name;
    private String dataType;



    public coCoMM_AttributeTypeElement(
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


}