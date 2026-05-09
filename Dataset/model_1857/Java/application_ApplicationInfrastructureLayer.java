





import java.util.List;
import java.util.ArrayList;

public class application_ApplicationInfrastructureLayer  {

    private String name;
    private String uid;



    public application_ApplicationInfrastructureLayer(
        String name,        String uid    ) {
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