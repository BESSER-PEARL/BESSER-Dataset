





import java.util.List;
import java.util.ArrayList;

public class jsm_AbstractMResource  {

    private String name;
    private boolean derived;





    private List<jsm_AbstractMResource> jsm_abstractmresources;




    private jsm_MPackage jsm_mpackage;




    private jsm_MPackage jsm_mpackage;




    private List<jsm_AbstractMResource> jsm_abstractmresources;


    public jsm_AbstractMResource(
        String name,        boolean derived    ) {
        this.name = name;
        this.derived = derived;
        this.jsm_abstractmresources = new ArrayList<>();
        this.jsm_abstractmresources = new ArrayList<>();
    }

    public jsm_AbstractMResource(
        String name,        boolean derived        ArrayList<jsm_AbstractMResource> jsm_abstractmresources,        ArrayList<jsm_AbstractMResource> jsm_abstractmresources    ) {
        this.name = name;
        this.derived = derived;
        this.jsm_abstractmresources = jsm_abstractmresources;
        this.jsm_abstractmresources = jsm_abstractmresources;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getDerived() {
        return derived;
    }

    public void setDerived(boolean derived) {
        this.derived = derived;
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
    public jsm_MPackage getJsm_mpackage() {
        return jsm_mpackage;
    }

    public void setJsm_mpackage(jsm_MPackage jsm_mpackage) {
        this.jsm_mpackage = jsm_mpackage;
    }
    public List<jsm_AbstractMResource> getJsm_abstractmresources() {
        return jsm_abstractmresources;
    }

    public void addJsm_abstractmresource(Jsm_abstractmresource jsm_abstractmresource) {
        this.jsm_abstractmresources.add(jsm_abstractmresource);
    }

}