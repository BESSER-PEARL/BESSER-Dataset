





import java.util.List;
import java.util.ArrayList;

public class UML2_Profile extends Package {






    private List<UML2_Stereotype> uml2_stereotypes;




    private UML2_ProfileApplication uml2_profileapplication;




    private List<UML2_PackageImport> uml2_packageimports;




    private List<UML2_ElementImport> uml2_elementimports;


    public UML2_Profile(
    ) {
        super(
        );
        this.uml2_stereotypes = new ArrayList<>();
        this.uml2_packageimports = new ArrayList<>();
        this.uml2_elementimports = new ArrayList<>();
    }

    public UML2_Profile(
        ArrayList<UML2_Stereotype> uml2_stereotypes,        ArrayList<UML2_PackageImport> uml2_packageimports,        ArrayList<UML2_ElementImport> uml2_elementimports    ) {
        this.uml2_stereotypes = uml2_stereotypes;
        this.uml2_packageimports = uml2_packageimports;
        this.uml2_elementimports = uml2_elementimports;
    }


    public List<UML2_Stereotype> getUml2_stereotypes() {
        return uml2_stereotypes;
    }

    public void addUml2_stereotype(Uml2_stereotype uml2_stereotype) {
        this.uml2_stereotypes.add(uml2_stereotype);
    }
    public UML2_ProfileApplication getUml2_profileapplication() {
        return uml2_profileapplication;
    }

    public void setUml2_profileapplication(UML2_ProfileApplication uml2_profileapplication) {
        this.uml2_profileapplication = uml2_profileapplication;
    }
    public List<UML2_PackageImport> getUml2_packageimports() {
        return uml2_packageimports;
    }

    public void addUml2_packageimport(Uml2_packageimport uml2_packageimport) {
        this.uml2_packageimports.add(uml2_packageimport);
    }
    public List<UML2_ElementImport> getUml2_elementimports() {
        return uml2_elementimports;
    }

    public void addUml2_elementimport(Uml2_elementimport uml2_elementimport) {
        this.uml2_elementimports.add(uml2_elementimport);
    }

}