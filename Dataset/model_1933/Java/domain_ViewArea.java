





import java.util.List;
import java.util.ArrayList;

public class domain_ViewArea extends Orderable, ViewElement {

    private String name;
    private String uid;



    public domain_ViewArea(
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


}