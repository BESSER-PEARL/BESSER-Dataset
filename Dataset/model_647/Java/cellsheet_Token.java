





import java.util.List;
import java.util.ArrayList;

public class cellsheet_Token  {

    private String value;





    private cellsheet_EStringToTokenEntry cellsheet_estringtotokenentry;


    public cellsheet_Token(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public cellsheet_EStringToTokenEntry getCellsheet_estringtotokenentry() {
        return cellsheet_estringtotokenentry;
    }

    public void setCellsheet_estringtotokenentry(cellsheet_EStringToTokenEntry cellsheet_estringtotokenentry) {
        this.cellsheet_estringtotokenentry = cellsheet_estringtotokenentry;
    }

}