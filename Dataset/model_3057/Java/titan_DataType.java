





import java.util.List;
import java.util.ArrayList;

public class titan_DataType extends Feature {

    private String type;





    private titan_MultiDataType titan_multidatatype;


    public titan_DataType(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public titan_MultiDataType getTitan_multidatatype() {
        return titan_multidatatype;
    }

    public void setTitan_multidatatype(titan_MultiDataType titan_multidatatype) {
        this.titan_multidatatype = titan_multidatatype;
    }

}