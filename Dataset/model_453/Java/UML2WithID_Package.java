





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Package extends PackageableElement, Namespace {






    private List<UML2WithID_Package> uml2withid_packages;




    private UML2WithID_PackageImport uml2withid_packageimport;




    private UML2WithID_Type uml2withid_type;




    private List<UML2WithID_Type> uml2withid_types;




    private UML2WithID_Package uml2withid_package;




    private List<UML2WithID_PackageableElement> uml2withid_packageableelements;


    public UML2WithID_Package(
    ) {
        super(
        );
        this.uml2withid_packages = new ArrayList<>();
        this.uml2withid_types = new ArrayList<>();
        this.uml2withid_packageableelements = new ArrayList<>();
    }

    public UML2WithID_Package(
        ArrayList<UML2WithID_Package> uml2withid_packages,        ArrayList<UML2WithID_Type> uml2withid_types,        ArrayList<UML2WithID_PackageableElement> uml2withid_packageableelements    ) {
        this.uml2withid_packages = uml2withid_packages;
        this.uml2withid_types = uml2withid_types;
        this.uml2withid_packageableelements = uml2withid_packageableelements;
    }


    public List<UML2WithID_Package> getUml2withid_packages() {
        return uml2withid_packages;
    }

    public void addUml2withid_package(Uml2withid_package uml2withid_package) {
        this.uml2withid_packages.add(uml2withid_package);
    }
    public UML2WithID_PackageImport getUml2withid_packageimport() {
        return uml2withid_packageimport;
    }

    public void setUml2withid_packageimport(UML2WithID_PackageImport uml2withid_packageimport) {
        this.uml2withid_packageimport = uml2withid_packageimport;
    }
    public UML2WithID_Type getUml2withid_type() {
        return uml2withid_type;
    }

    public void setUml2withid_type(UML2WithID_Type uml2withid_type) {
        this.uml2withid_type = uml2withid_type;
    }
    public List<UML2WithID_Type> getUml2withid_types() {
        return uml2withid_types;
    }

    public void addUml2withid_type(Uml2withid_type uml2withid_type) {
        this.uml2withid_types.add(uml2withid_type);
    }
    public UML2WithID_Package getUml2withid_package() {
        return uml2withid_package;
    }

    public void setUml2withid_package(UML2WithID_Package uml2withid_package) {
        this.uml2withid_package = uml2withid_package;
    }
    public List<UML2WithID_PackageableElement> getUml2withid_packageableelements() {
        return uml2withid_packageableelements;
    }

    public void addUml2withid_packageableelement(Uml2withid_packageableelement uml2withid_packageableelement) {
        this.uml2withid_packageableelements.add(uml2withid_packageableelement);
    }

}