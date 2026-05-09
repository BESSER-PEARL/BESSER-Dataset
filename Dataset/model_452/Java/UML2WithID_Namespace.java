





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Namespace extends NamedElement {






    private List<UML2WithID_ElementImport> uml2withid_elementimports;




    private UML2WithID_PackageImport uml2withid_packageimport;




    private List<UML2WithID_PackageImport> uml2withid_packageimports;




    private UML2WithID_ElementImport uml2withid_elementimport;




    private List<UML2WithID_NamedElement> uml2withid_namedelements;


    public UML2WithID_Namespace(
    ) {
        super(
        );
        this.uml2withid_elementimports = new ArrayList<>();
        this.uml2withid_packageimports = new ArrayList<>();
        this.uml2withid_namedelements = new ArrayList<>();
    }

    public UML2WithID_Namespace(
        ArrayList<UML2WithID_ElementImport> uml2withid_elementimports,        ArrayList<UML2WithID_PackageImport> uml2withid_packageimports,        ArrayList<UML2WithID_NamedElement> uml2withid_namedelements    ) {
        this.uml2withid_elementimports = uml2withid_elementimports;
        this.uml2withid_packageimports = uml2withid_packageimports;
        this.uml2withid_namedelements = uml2withid_namedelements;
    }


    public List<UML2WithID_ElementImport> getUml2withid_elementimports() {
        return uml2withid_elementimports;
    }

    public void addUml2withid_elementimport(Uml2withid_elementimport uml2withid_elementimport) {
        this.uml2withid_elementimports.add(uml2withid_elementimport);
    }
    public UML2WithID_PackageImport getUml2withid_packageimport() {
        return uml2withid_packageimport;
    }

    public void setUml2withid_packageimport(UML2WithID_PackageImport uml2withid_packageimport) {
        this.uml2withid_packageimport = uml2withid_packageimport;
    }
    public List<UML2WithID_PackageImport> getUml2withid_packageimports() {
        return uml2withid_packageimports;
    }

    public void addUml2withid_packageimport(Uml2withid_packageimport uml2withid_packageimport) {
        this.uml2withid_packageimports.add(uml2withid_packageimport);
    }
    public UML2WithID_ElementImport getUml2withid_elementimport() {
        return uml2withid_elementimport;
    }

    public void setUml2withid_elementimport(UML2WithID_ElementImport uml2withid_elementimport) {
        this.uml2withid_elementimport = uml2withid_elementimport;
    }
    public List<UML2WithID_NamedElement> getUml2withid_namedelements() {
        return uml2withid_namedelements;
    }

    public void addUml2withid_namedelement(Uml2withid_namedelement uml2withid_namedelement) {
        this.uml2withid_namedelements.add(uml2withid_namedelement);
    }

}