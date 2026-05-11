





import java.util.List;
import java.util.ArrayList;

public class type_Parameter extends TypePointer {

    private int order;
    private String name;
    private String uid;





    private type_Operation type_operation;


    public type_Parameter(
        int order,        String name,        String uid    ) {
        super(
        );
        this.order = order;
        this.name = name;
        this.uid = uid;
    }


    public int getOrder() {
        return order;
    }

    public void setOrder(int order) {
        this.order = order;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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