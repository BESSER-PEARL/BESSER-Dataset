





import java.util.List;
import java.util.ArrayList;

public class Java_Return extends Statement {

    private String objectId;
    private String fieldName;



    public Java_Return(
        String objectId,        String fieldName    ) {
        super(
        );
        this.objectId = objectId;
        this.fieldName = fieldName;
    }


    public String getObjectid() {
        return objectId;
    }

    public void setObjectid(String objectId) {
        this.objectId = objectId;
    }
    public String getFieldname() {
        return fieldName;
    }

    public void setFieldname(String fieldName) {
        this.fieldName = fieldName;
    }


}