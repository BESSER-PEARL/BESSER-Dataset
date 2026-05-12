





import java.util.List;
import java.util.ArrayList;

public class UML2_Package extends PackageableElement, Namespace {






    private UML2_Package uml2_package;




    private List<UML2_PackageableElement> uml2_packageableelements;




    private UML2_Type uml2_type;




    private List<UML2_Type> uml2_types;




    private UML2_Package uml2_package;




    private UML2_PackageImport uml2_packageimport;


    public UML2_Package(
    ) {
        super(
        );
        this.uml2_packageableelements = new ArrayList<>();
        this.uml2_types = new ArrayList<>();
    }

    public UML2_Package(
        ArrayList<UML2_PackageableElement> uml2_packageableelements,        ArrayList<UML2_Type> uml2_types    ) {
        this.uml2_packageableelements = uml2_packageableelements;
        this.uml2_types = uml2_types;
    }


    public UML2_Package getUml2_package() {
        return uml2_package;
    }

    public void setUml2_package(UML2_Package uml2_package) {
        this.uml2_package = uml2_package;
    }
    public List<UML2_PackageableElement> getUml2_packageableelements() {
        return uml2_packageableelements;
    }

    public void addUml2_packageableelement(Uml2_packageableelement uml2_packageableelement) {
        this.uml2_packageableelements.add(uml2_packageableelement);
    }
    public UML2_Type getUml2_type() {
        return uml2_type;
    }

    public void setUml2_type(UML2_Type uml2_type) {
        this.uml2_type = uml2_type;
    }
    public List<UML2_Type> getUml2_types() {
        return uml2_types;
    }

    public void addUml2_type(Uml2_type uml2_type) {
        this.uml2_types.add(uml2_type);
    }
    public UML2_Package getUml2_package() {
        return uml2_package;
    }

    public void setUml2_package(UML2_Package uml2_package) {
        this.uml2_package = uml2_package;
    }
    public UML2_PackageImport getUml2_packageimport() {
        return uml2_packageimport;
    }

    public void setUml2_packageimport(UML2_PackageImport uml2_packageimport) {
        this.uml2_packageimport = uml2_packageimport;
    }

}