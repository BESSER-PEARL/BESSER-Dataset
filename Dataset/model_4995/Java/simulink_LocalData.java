





import java.util.List;
import java.util.ArrayList;

public class simulink_LocalData extends Data {

    private String dataType;



    public simulink_LocalData(
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