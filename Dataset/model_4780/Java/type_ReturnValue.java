





import java.util.List;
import java.util.ArrayList;

public class type_ReturnValue extends TypePointer {

    private String uid;





    private type_Operation type_operation;


    public type_ReturnValue(
        String uid    ) {
        super(
        );
        this.uid = uid;
    }


    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }

    public type_Operation getType_operation() {
        return type_operation;
    }

    public void setType_operation(type_Operation type_operation) {
        this.type_operation = type_operation;
    }

}