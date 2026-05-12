





import java.util.List;
import java.util.ArrayList;

public class connection_RegexpFileConnection extends FileConnection {

    private String FieldSeparatorType;



    public connection_RegexpFileConnection(
        String FieldSeparatorType    ) {
        super(
        );
        this.FieldSeparatorType = FieldSeparatorType;
    }


    public String getFieldseparatortype() {
        return FieldSeparatorType;
    }

    public void setFieldseparatortype(String FieldSeparatorType) {
        this.FieldSeparatorType = FieldSeparatorType;
    }


}