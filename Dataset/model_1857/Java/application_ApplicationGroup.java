





import java.util.List;
import java.util.ArrayList;

public class application_ApplicationGroup  {

    private String uid;
    private String name;



    public application_ApplicationGroup(
        String uid,        String name    ) {
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