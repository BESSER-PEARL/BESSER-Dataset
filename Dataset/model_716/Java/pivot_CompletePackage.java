





import java.util.List;
import java.util.ArrayList;

public class pivot_CompletePackage extends NamedElement {






    private pivot_CompleteModel pivot_completemodel;




    private pivot_CompletePackage pivot_completepackage;




    private pivot_CompletePackage pivot_completepackage;




    private List<pivot_CompleteClass> pivot_completeclasss;




    private pivot_CompleteClass pivot_completeclass;




    private pivot_CompleteModel pivot_completemodel;


    public pivot_CompletePackage(
    ) {
        super(
        );
        this.pivot_completeclasss = new ArrayList<>();
    }

    public pivot_CompletePackage(
        ArrayList<pivot_CompleteClass> pivot_completeclasss    ) {
        this.pivot_completeclasss = pivot_completeclasss;
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
    public pivot_CompletePackage getPivot_completepackage() {
        return pivot_completepackage;
    }

    public void setPivot_completepackage(pivot_CompletePackage pivot_completepackage) {
        this.pivot_completepackage = pivot_completepackage;
    }
    public List<pivot_CompleteClass> getPivot_completeclasss() {
        return pivot_completeclasss;
    }

    public void addPivot_completeclass(Pivot_completeclass pivot_completeclass) {
        this.pivot_completeclasss.add(pivot_completeclass);
    }
    public pivot_CompleteClass getPivot_completeclass() {
        return pivot_completeclass;
    }

    public void setPivot_completeclass(pivot_CompleteClass pivot_completeclass) {
        this.pivot_completeclass = pivot_completeclass;
    }
    public pivot_CompleteModel getPivot_completemodel() {
        return pivot_completemodel;
    }

    public void setPivot_completemodel(pivot_CompleteModel pivot_completemodel) {
        this.pivot_completemodel = pivot_completemodel;
    }

}