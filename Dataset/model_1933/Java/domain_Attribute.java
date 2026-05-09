





import java.util.List;
import java.util.ArrayList;

public class domain_Attribute extends Categorized, TypePointer {

    private boolean pk;
    private String name;
    private String uid;



    public domain_Attribute(
        boolean pk,        String name,        String uid    ) {
        super(
        );
        this.pk = pk;
        this.name = name;
        this.uid = uid;
    }


    public boolean getPk() {
        return pk;
    }

    public void setPk(boolean pk) {
        this.pk = pk;
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


}