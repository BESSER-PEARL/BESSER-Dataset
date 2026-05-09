





import java.util.List;
import java.util.ArrayList;

public class domain_PREUpdateTrigger extends Trigger {

    private String uid;



    public domain_PREUpdateTrigger(
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