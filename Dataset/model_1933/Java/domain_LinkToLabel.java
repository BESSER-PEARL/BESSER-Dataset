





import java.util.List;
import java.util.ArrayList;

public class domain_LinkToLabel  {

    private String uid;





    private domain_CanvasView domain_canvasview;




    private domain_Label domain_label;


    public domain_LinkToLabel(
        String uid    ) {
        this.uid = uid;
    }


    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }

    public domain_CanvasView getDomain_canvasview() {
        return domain_canvasview;
    }

    public void setDomain_canvasview(domain_CanvasView domain_canvasview) {
        this.domain_canvasview = domain_canvasview;
    }
    public domain_Label getDomain_label() {
        return domain_label;
    }

    public void setDomain_label(domain_Label domain_label) {
        this.domain_label = domain_label;
    }

}