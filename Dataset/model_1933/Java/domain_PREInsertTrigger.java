





import java.util.List;
import java.util.ArrayList;

public class domain_PREInsertTrigger extends Trigger {

    private String uid;



    public domain_PREInsertTrigger(
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