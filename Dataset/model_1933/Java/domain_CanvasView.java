





import java.util.List;
import java.util.ArrayList;

public class domain_CanvasView  {

    private String uid;





    private domain_LayerHolder domain_layerholder;




    private domain_ViewArea domain_viewarea;




    private domain_ViewArea domain_viewarea;




    private domain_EObject domain_eobject;


    public domain_CanvasView(
        String uid    ) {
        this.uid = uid;
    }


    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }

    public domain_LayerHolder getDomain_layerholder() {
        return domain_layerholder;
    }

    public void setDomain_layerholder(domain_LayerHolder domain_layerholder) {
        this.domain_layerholder = domain_layerholder;
    }
    public domain_ViewArea getDomain_viewarea() {
        return domain_viewarea;
    }

    public void setDomain_viewarea(domain_ViewArea domain_viewarea) {
        this.domain_viewarea = domain_viewarea;
    }
    public domain_ViewArea getDomain_viewarea() {
        return domain_viewarea;
    }

    public void setDomain_viewarea(domain_ViewArea domain_viewarea) {
        this.domain_viewarea = domain_viewarea;
    }
    public domain_EObject getDomain_eobject() {
        return domain_eobject;
    }

    public void setDomain_eobject(domain_EObject domain_eobject) {
        this.domain_eobject = domain_eobject;
    }

}