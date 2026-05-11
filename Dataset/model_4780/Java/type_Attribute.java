





import java.util.List;
import java.util.ArrayList;

public class type_Attribute extends TypePointer, Categorized {

    private boolean pk;
    private String uid;
    private String name;





    private type_Type type_type;


    public type_Attribute(
        boolean pk,        String uid,        String name    ) {
        super(
        );
        this.pk = pk;
        this.uid = uid;
        this.name = name;
    }


    public boolean getPk() {
        return pk;
    }

    public void setPk(boolean pk) {
        this.pk = pk;
    }
    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public type_Type getType_type() {
        return type_type;
    }

    public void setType_type(type_Type type_type) {
        this.type_type = type_type;
    }

}