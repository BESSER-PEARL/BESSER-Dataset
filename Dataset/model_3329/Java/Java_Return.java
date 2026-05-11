





import java.util.List;
import java.util.ArrayList;

public class Java_Return extends Statement {

    private String fieldName;
    private String objectId;



    public Java_Return(
        String fieldName,        String objectId    ) {
        super(
        );
        this.fieldName = fieldName;
        this.objectId = objectId;
    }


    public String getFieldname() {
        return fieldName;
    }

    public void setFieldname(String fieldName) {
        this.fieldName = fieldName;
    }
    public String getObjectid() {
        return objectId;
    }

    public void setObjectid(String objectId) {
        this.objectId = objectId;
    }


}