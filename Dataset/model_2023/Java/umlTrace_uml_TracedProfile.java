





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedProfile extends TracedPackage {






    private List<uml_TracedPackageImport> uml_tracedpackageimports;




    private List<uml_TracedElementImport> uml_tracedelementimports;


    public umlTrace_uml_TracedProfile(
    ) {
        super(
        );
        this.uml_tracedpackageimports = new ArrayList<>();
        this.uml_tracedelementimports = new ArrayList<>();
    }

    public umlTrace_uml_TracedProfile(
        ArrayList<uml_TracedPackageImport> uml_tracedpackageimports,        ArrayList<uml_TracedElementImport> uml_tracedelementimports    ) {
        this.uml_tracedpackageimports = uml_tracedpackageimports;
        this.uml_tracedelementimports = uml_tracedelementimports;
    }


    public List<uml_TracedPackageImport> getUml_tracedpackageimports() {
        return uml_tracedpackageimports;
    }

    public void addUml_tracedpackageimport(Uml_tracedpackageimport uml_tracedpackageimport) {
        this.uml_tracedpackageimports.add(uml_tracedpackageimport);
    }
    public List<uml_TracedElementImport> getUml_tracedelementimports() {
        return uml_tracedelementimports;
    }

    public void addUml_tracedelementimport(Uml_tracedelementimport uml_tracedelementimport) {
        this.uml_tracedelementimports.add(uml_tracedelementimport);
    }

}