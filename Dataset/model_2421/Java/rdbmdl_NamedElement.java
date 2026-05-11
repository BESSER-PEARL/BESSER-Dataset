





import java.util.List;
import java.util.ArrayList;

public class rdbmdl_NamedElement extends Element {

    private String uid;
    private String name;



    public rdbmdl_NamedElement(
        String uid,        String name    ) {
        super(
        );
        this.uid = uid;
        this.name = name;
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


}