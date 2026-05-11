





import java.util.List;
import java.util.ArrayList;

public class model_AbstractMResource  {

    private boolean derived;
    private String name;





    private List<model_AbstractMResource> model_abstractmresources;




    private model_MPackage model_mpackage;




    private model_AbstractMResource model_abstractmresource;




    private model_MPackage model_mpackage;


    public model_AbstractMResource(
        boolean derived,        String name    ) {
        this.derived = derived;
        this.name = name;
        this.model_abstractmresources = new ArrayList<>();
    }

    public model_AbstractMResource(
        boolean derived,        String name        ArrayList<model_AbstractMResource> model_abstractmresources    ) {
        this.derived = derived;
        this.name = name;
        this.model_abstractmresources = model_abstractmresources;
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

    public List<model_AbstractMResource> getModel_abstractmresources() {
        return model_abstractmresources;
    }

    public void addModel_abstractmresource(Model_abstractmresource model_abstractmresource) {
        this.model_abstractmresources.add(model_abstractmresource);
    }
    public model_MPackage getModel_mpackage() {
        return model_mpackage;
    }

    public void setModel_mpackage(model_MPackage model_mpackage) {
        this.model_mpackage = model_mpackage;
    }
    public model_AbstractMResource getModel_abstractmresource() {
        return model_abstractmresource;
    }

    public void setModel_abstractmresource(model_AbstractMResource model_abstractmresource) {
        this.model_abstractmresource = model_abstractmresource;
    }
    public model_MPackage getModel_mpackage() {
        return model_mpackage;
    }

    public void setModel_mpackage(model_MPackage model_mpackage) {
        this.model_mpackage = model_mpackage;
    }

}