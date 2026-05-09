





import java.util.List;
import java.util.ArrayList;

public class domain_DeleteTrigger extends Trigger, ProxiesList {

    private String uid;



    public domain_DeleteTrigger(
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