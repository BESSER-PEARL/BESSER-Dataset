





import java.util.List;
import java.util.ArrayList;

public class domain_ViewInheritance  {

    private String uid;





    private domain_CanvasFrame domain_canvasframe;




    private domain_Views domain_views;


    public domain_ViewInheritance(
        String uid    ) {
        this.uid = uid;
    }


    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }

    public domain_CanvasFrame getDomain_canvasframe() {
        return domain_canvasframe;
    }

    public void setDomain_canvasframe(domain_CanvasFrame domain_canvasframe) {
        this.domain_canvasframe = domain_canvasframe;
    }
    public domain_Views getDomain_views() {
        return domain_views;
    }

    public void setDomain_views(domain_Views domain_views) {
        this.domain_views = domain_views;
    }

}