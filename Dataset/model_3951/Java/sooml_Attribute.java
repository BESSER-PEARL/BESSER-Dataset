





import java.util.List;
import java.util.ArrayList;

public class sooml_Attribute extends StructuralFeature {

    private String dataType;



    public sooml_Attribute(
        String dataType    ) {
        super(
        );
        this.dataType = dataType;
    }


    public String getDatatype() {
        return dataType;
    }

    public void setDatatype(String dataType) {
        this.dataType = dataType;
    }


}