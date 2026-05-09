





import java.util.List;
import java.util.ArrayList;

public class domain_SearchTrigger extends Trigger, ProxiesList {

    private String uid;



    public domain_SearchTrigger(
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


}