





import java.util.List;
import java.util.ArrayList;

public class SimpleRDBMS_RdbmsColumn extends RdbmsModelElement {

    private String rdbmsType;



    public SimpleRDBMS_RdbmsColumn(
        String rdbmsType    ) {
        super(
        );
        this.rdbmsType = rdbmsType;
    }


    public String getRdbmstype() {
        return rdbmsType;
    }

    public void setRdbmstype(String rdbmsType) {
        this.rdbmsType = rdbmsType;
    }


}