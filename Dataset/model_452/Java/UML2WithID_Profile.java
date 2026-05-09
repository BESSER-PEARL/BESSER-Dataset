





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Profile extends Package {






    private List<UML2WithID_PackageImport> uml2withid_packageimports;




    private List<UML2WithID_ElementImport> uml2withid_elementimports;




    private List<UML2WithID_Stereotype> uml2withid_stereotypes;


    public UML2WithID_Profile(
    ) {
        super(
        );
        this.uml2withid_packageimports = new ArrayList<>();
        this.uml2withid_elementimports = new ArrayList<>();
        this.uml2withid_stereotypes = new ArrayList<>();
    }

    public UML2WithID_Profile(
        ArrayList<UML2WithID_PackageImport> uml2withid_packageimports,        ArrayList<UML2WithID_ElementImport> uml2withid_elementimports,        ArrayList<UML2WithID_Stereotype> uml2withid_stereotypes    ) {
        this.uml2withid_packageimports = uml2withid_packageimports;
        this.uml2withid_elementimports = uml2withid_elementimports;
        this.uml2withid_stereotypes = uml2withid_stereotypes;
    }


    public List<UML2WithID_PackageImport> getUml2withid_packageimports() {
        return uml2withid_packageimports;
    }

    public void addUml2withid_packageimport(Uml2withid_packageimport uml2withid_packageimport) {
        this.uml2withid_packageimports.add(uml2withid_packageimport);
    }
    public List<UML2WithID_ElementImport> getUml2withid_elementimports() {
        return uml2withid_elementimports;
    }

    public void addUml2withid_elementimport(Uml2withid_elementimport uml2withid_elementimport) {
        this.uml2withid_elementimports.add(uml2withid_elementimport);
    }
    public List<UML2WithID_Stereotype> getUml2withid_stereotypes() {
        return uml2withid_stereotypes;
    }

    public void addUml2withid_stereotype(Uml2withid_stereotype uml2withid_stereotype) {
        this.uml2withid_stereotypes.add(uml2withid_stereotype);
    }

}