





import java.util.List;
import java.util.ArrayList;

public class domain_ViewPort extends Orderable, ViewElement {

    private String uid;
    private String name;





    private domain_ViewInheritance domain_viewinheritance;


    public domain_ViewPort(
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

    public domain_ViewInheritance getDomain_viewinheritance() {
        return domain_viewinheritance;
    }

    public void setDomain_viewinheritance(domain_ViewInheritance domain_viewinheritance) {
        this.domain_viewinheritance = domain_viewinheritance;
    }

}