





import java.util.List;
import java.util.ArrayList;

public class domain_LinkToMessage  {

    private String uid;





    private domain_MessageElement domain_messageelement;




    private domain_CanvasView domain_canvasview;


    public domain_LinkToMessage(
        String uid    ) {
        this.uid = uid;
    }


    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }

    public domain_MessageElement getDomain_messageelement() {
        return domain_messageelement;
    }

    public void setDomain_messageelement(domain_MessageElement domain_messageelement) {
        this.domain_messageelement = domain_messageelement;
    }
    public domain_CanvasView getDomain_canvasview() {
        return domain_canvasview;
    }

    public void setDomain_canvasview(domain_CanvasView domain_canvasview) {
        this.domain_canvasview = domain_canvasview;
    }

}