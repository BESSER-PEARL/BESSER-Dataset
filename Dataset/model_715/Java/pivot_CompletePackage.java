





import java.util.List;
import java.util.ArrayList;

public class pivot_CompletePackage extends NamedElement {






    private pivot_CompleteModel pivot_completemodel;




    private pivot_CompletePackage pivot_completepackage;




    private List<pivot_CompletePackage> pivot_completepackages;




    private pivot_CompleteModel pivot_completemodel;


    public pivot_CompletePackage(
    ) {
        super(
        );
        this.pivot_completepackages = new ArrayList<>();
    }

    public pivot_CompletePackage(
        ArrayList<pivot_CompletePackage> pivot_completepackages    ) {
        this.pivot_completepackages = pivot_completepackages;
    }


    public pivot_CompleteModel getPivot_completemodel() {
        return pivot_completemodel;
    }

    public void setPivot_completemodel(pivot_CompleteModel pivot_completemodel) {
        this.pivot_completemodel = pivot_completemodel;
    }
    public pivot_CompletePackage getPivot_completepackage() {
        return pivot_completepackage;
    }

    public void setPivot_completepackage(pivot_CompletePackage pivot_completepackage) {
        this.pivot_completepackage = pivot_completepackage;
    }
    public List<pivot_CompletePackage> getPivot_completepackages() {
        return pivot_completepackages;
    }

    public void addPivot_completepackage(Pivot_completepackage pivot_completepackage) {
        this.pivot_completepackages.add(pivot_completepackage);
    }
    public pivot_CompleteModel getPivot_completemodel() {
        return pivot_completemodel;
    }

    public void setPivot_completemodel(pivot_CompleteModel pivot_completemodel) {
        this.pivot_completemodel = pivot_completemodel;
    }

}