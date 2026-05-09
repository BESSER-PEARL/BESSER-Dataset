





import java.util.List;
import java.util.ArrayList;

public class domain_ViewPortTrigger extends Trigger {

    private String uid;





    private domain_ViewPort domain_viewport;


    public domain_ViewPortTrigger(
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

    public domain_ViewPort getDomain_viewport() {
        return domain_viewport;
    }

    public void setDomain_viewport(domain_ViewPort domain_viewport) {
        this.domain_viewport = domain_viewport;
    }

}