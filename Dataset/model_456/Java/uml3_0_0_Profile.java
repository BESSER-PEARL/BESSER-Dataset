





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_Profile extends Package {






    private List<uml3_0_0_PackageImport> uml3_0_0_packageimports;




    private List<uml3_0_0_Stereotype> uml3_0_0_stereotypes;




    private uml3_0_0_ProfileApplication uml3_0_0_profileapplication;




    private List<uml3_0_0_ElementImport> uml3_0_0_elementimports;


    public uml3_0_0_Profile(
    ) {
        super(
        );
        this.uml3_0_0_packageimports = new ArrayList<>();
        this.uml3_0_0_stereotypes = new ArrayList<>();
        this.uml3_0_0_elementimports = new ArrayList<>();
    }

    public uml3_0_0_Profile(
        ArrayList<uml3_0_0_PackageImport> uml3_0_0_packageimports,        ArrayList<uml3_0_0_Stereotype> uml3_0_0_stereotypes,        ArrayList<uml3_0_0_ElementImport> uml3_0_0_elementimports    ) {
        this.uml3_0_0_packageimports = uml3_0_0_packageimports;
        this.uml3_0_0_stereotypes = uml3_0_0_stereotypes;
        this.uml3_0_0_elementimports = uml3_0_0_elementimports;
    }


    public List<uml3_0_0_PackageImport> getUml3_0_0_packageimports() {
        return uml3_0_0_packageimports;
    }

    public void addUml3_0_0_packageimport(Uml3_0_0_packageimport uml3_0_0_packageimport) {
        this.uml3_0_0_packageimports.add(uml3_0_0_packageimport);
    }
    public List<uml3_0_0_Stereotype> getUml3_0_0_stereotypes() {
        return uml3_0_0_stereotypes;
    }

    public void addUml3_0_0_stereotype(Uml3_0_0_stereotype uml3_0_0_stereotype) {
        this.uml3_0_0_stereotypes.add(uml3_0_0_stereotype);
    }
    public uml3_0_0_ProfileApplication getUml3_0_0_profileapplication() {
        return uml3_0_0_profileapplication;
    }

    public void setUml3_0_0_profileapplication(uml3_0_0_ProfileApplication uml3_0_0_profileapplication) {
        this.uml3_0_0_profileapplication = uml3_0_0_profileapplication;
    }
    public List<uml3_0_0_ElementImport> getUml3_0_0_elementimports() {
        return uml3_0_0_elementimports;
    }

    public void addUml3_0_0_elementimport(Uml3_0_0_elementimport uml3_0_0_elementimport) {
        this.uml3_0_0_elementimports.add(uml3_0_0_elementimport);
    }

}