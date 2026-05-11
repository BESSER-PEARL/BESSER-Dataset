





import java.util.List;
import java.util.ArrayList;

public class jsm_AbstractMResource  {

    private boolean derived;
    private String name;





    private jsm_MPackage jsm_mpackage;




    private jsm_AbstractMResource jsm_abstractmresource;




    private List<jsm_AbstractMResource> jsm_abstractmresources;




    private jsm_MPackage jsm_mpackage;


    public jsm_AbstractMResource(
        boolean derived,        String name    ) {
        this.derived = derived;
        this.name = name;
        this.jsm_abstractmresources = new ArrayList<>();
    }

    public jsm_AbstractMResource(
        boolean derived,        String name        ArrayList<jsm_AbstractMResource> jsm_abstractmresources    ) {
        this.derived = derived;
        this.name = name;
        this.jsm_abstractmresources = jsm_abstractmresources;
    }

    public boolean getDerived() {
        return derived;
    }

    public void setDerived(boolean derived) {
        this.derived = derived;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public jsm_MPackage getJsm_mpackage() {
        return jsm_mpackage;
    }

    public void setJsm_mpackage(jsm_MPackage jsm_mpackage) {
        this.jsm_mpackage = jsm_mpackage;
    }
    public jsm_AbstractMResource getJsm_abstractmresource() {
        return jsm_abstractmresource;
    }

    public void setJsm_abstractmresource(jsm_AbstractMResource jsm_abstractmresource) {
        this.jsm_abstractmresource = jsm_abstractmresource;
    }
    public List<jsm_AbstractMResource> getJsm_abstractmresources() {
        return jsm_abstractmresources;
    }

    public void addJsm_abstractmresource(Jsm_abstractmresource jsm_abstractmresource) {
        this.jsm_abstractmresources.add(jsm_abstractmresource);
    }
    public jsm_MPackage getJsm_mpackage() {
        return jsm_mpackage;
    }

    public void setJsm_mpackage(jsm_MPackage jsm_mpackage) {
        this.jsm_mpackage = jsm_mpackage;
    }

}