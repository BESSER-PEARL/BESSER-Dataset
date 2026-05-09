





import java.util.List;
import java.util.ArrayList;

public class domain_CanvasFrame extends StyleElement {

    private String uid;
    private String name;





    private domain_Views domain_views;


    public domain_CanvasFrame(
        String uid,        String name    ) {
        super(
        );
        this.uid = uid;
        this.name = name;
    }


    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public domain_Views getDomain_views() {
        return domain_views;
    }

    public void setDomain_views(domain_Views domain_views) {
        this.domain_views = domain_views;
    }

}