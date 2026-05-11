





import java.util.List;
import java.util.ArrayList;

public class type_Operation extends Categorized, Secured {

    private String name;
    private String uid;





    private type_Type type_type;


    public type_Operation(
        String name,        String uid    ) {
        super(
        );
        this.name = name;
        this.uid = uid;
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

    public type_Type getType_type() {
        return type_type;
    }

    public void setType_type(type_Type type_type) {
        this.type_type = type_type;
    }

}