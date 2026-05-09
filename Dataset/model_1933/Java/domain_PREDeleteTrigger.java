





import java.util.List;
import java.util.ArrayList;

public class domain_PREDeleteTrigger extends Trigger {

    private String uid;



    public domain_PREDeleteTrigger(
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