





import java.util.List;
import java.util.ArrayList;

public class domain_TabPagesInheritance  {

    private String uid;





    private domain_TabCanvas domain_tabcanvas;




    private domain_TabPage domain_tabpage;




    private domain_Views domain_views;


    public domain_TabPagesInheritance(
        String uid    ) {
        this.uid = uid;
    }


    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }

    public domain_TabCanvas getDomain_tabcanvas() {
        return domain_tabcanvas;
    }

    public void setDomain_tabcanvas(domain_TabCanvas domain_tabcanvas) {
        this.domain_tabcanvas = domain_tabcanvas;
    }
    public domain_TabPage getDomain_tabpage() {
        return domain_tabpage;
    }

    public void setDomain_tabpage(domain_TabPage domain_tabpage) {
        this.domain_tabpage = domain_tabpage;
    }
    public domain_Views getDomain_views() {
        return domain_views;
    }

    public void setDomain_views(domain_Views domain_views) {
        this.domain_views = domain_views;
    }

}