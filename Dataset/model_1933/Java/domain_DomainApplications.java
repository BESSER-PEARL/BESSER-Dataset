





import java.util.List;
import java.util.ArrayList;

public class domain_DomainApplications extends HTMLLayerHolder {

    private String uid;
    private String name;



    public domain_DomainApplications(
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