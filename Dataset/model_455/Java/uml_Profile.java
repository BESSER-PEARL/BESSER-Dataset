





import java.util.List;
import java.util.ArrayList;

public class uml_Profile extends Package {






    private List<uml_Stereotype> uml_stereotypes;




    private List<uml_ElementImport> uml_elementimports;




    private List<uml_PackageImport> uml_packageimports;




    private uml_ProfileApplication uml_profileapplication;


    public uml_Profile(
    ) {
        super(
        );
        this.uml_stereotypes = new ArrayList<>();
        this.uml_elementimports = new ArrayList<>();
        this.uml_packageimports = new ArrayList<>();
    }

    public uml_Profile(
        ArrayList<uml_Stereotype> uml_stereotypes,        ArrayList<uml_ElementImport> uml_elementimports,        ArrayList<uml_PackageImport> uml_packageimports    ) {
        this.uml_stereotypes = uml_stereotypes;
        this.uml_elementimports = uml_elementimports;
        this.uml_packageimports = uml_packageimports;
    }


    public List<uml_Stereotype> getUml_stereotypes() {
        return uml_stereotypes;
    }

    public void addUml_stereotype(Uml_stereotype uml_stereotype) {
        this.uml_stereotypes.add(uml_stereotype);
    }
    public List<uml_ElementImport> getUml_elementimports() {
        return uml_elementimports;
    }

    public void addUml_elementimport(Uml_elementimport uml_elementimport) {
        this.uml_elementimports.add(uml_elementimport);
    }
    public List<uml_PackageImport> getUml_packageimports() {
        return uml_packageimports;
    }

    public void addUml_packageimport(Uml_packageimport uml_packageimport) {
        this.uml_packageimports.add(uml_packageimport);
    }
    public uml_ProfileApplication getUml_profileapplication() {
        return uml_profileapplication;
    }

    public void setUml_profileapplication(uml_ProfileApplication uml_profileapplication) {
        this.uml_profileapplication = uml_profileapplication;
    }

}