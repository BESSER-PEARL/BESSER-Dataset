





import java.util.List;
import java.util.ArrayList;

public class statemachine_Variable extends DataElement {

    private String dataType;



    public statemachine_Variable(
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