





import java.util.List;
import java.util.ArrayList;

public class cmof_Package extends PackageableElement, Namespace {

    private String URI;





    private cmof_Factory cmof_factory;




    private cmof_Package cmof_package;




    private List<cmof_PackageableElement> cmof_packageableelements;




    private cmof_Package cmof_package;


    public cmof_Package(
        String URI    ) {
        super(
        );
        this.URI = URI;
        this.cmof_packageableelements = new ArrayList<>();
    }

    public cmof_Package(
        String URI        ArrayList<cmof_PackageableElement> cmof_packageableelements    ) {
        this.URI = URI;
        this.cmof_packageableelements = cmof_packageableelements;
    }

    public String getUri() {
        return URI;
    }

    public void setUri(String URI) {
        this.URI = URI;
    }

    public cmof_Factory getCmof_factory() {
        return cmof_factory;
    }

    public void setCmof_factory(cmof_Factory cmof_factory) {
        this.cmof_factory = cmof_factory;
    }
    public cmof_Package getCmof_package() {
        return cmof_package;
    }

    public void setCmof_package(cmof_Package cmof_package) {
        this.cmof_package = cmof_package;
    }
    public List<cmof_PackageableElement> getCmof_packageableelements() {
        return cmof_packageableelements;
    }

    public void addCmof_packageableelement(Cmof_packageableelement cmof_packageableelement) {
        this.cmof_packageableelements.add(cmof_packageableelement);
    }
    public cmof_Package getCmof_package() {
        return cmof_package;
    }

    public void setCmof_package(cmof_Package cmof_package) {
        this.cmof_package = cmof_package;
    }

}