





import java.util.List;
import java.util.ArrayList;

public class umlMM_Class extends Classifier {






    private umlMM_Association umlmm_association;




    private umlMM_Association umlmm_association;




    private List<umlMM_Association> umlmm_associations;




    private List<umlMM_Association> umlmm_associations;




    private List<umlMM_Class> umlmm_classs;


    public umlMM_Class(
    ) {
        super(
        );
        this.umlmm_associations = new ArrayList<>();
        this.umlmm_associations = new ArrayList<>();
        this.umlmm_classs = new ArrayList<>();
    }

    public umlMM_Class(
        ArrayList<umlMM_Association> umlmm_associations,        ArrayList<umlMM_Association> umlmm_associations,        ArrayList<umlMM_Class> umlmm_classs    ) {
        this.umlmm_associations = umlmm_associations;
        this.umlmm_associations = umlmm_associations;
        this.umlmm_classs = umlmm_classs;
    }


    public umlMM_Association getUmlmm_association() {
        return umlmm_association;
    }

    public void setUmlmm_association(umlMM_Association umlmm_association) {
        this.umlmm_association = umlmm_association;
    }
    public umlMM_Association getUmlmm_association() {
        return umlmm_association;
    }

    public void setUmlmm_association(umlMM_Association umlmm_association) {
        this.umlmm_association = umlmm_association;
    }
    public List<umlMM_Association> getUmlmm_associations() {
        return umlmm_associations;
    }

    public void addUmlmm_association(Umlmm_association umlmm_association) {
        this.umlmm_associations.add(umlmm_association);
    }
    public List<umlMM_Association> getUmlmm_associations() {
        return umlmm_associations;
    }

    public void addUmlmm_association(Umlmm_association umlmm_association) {
        this.umlmm_associations.add(umlmm_association);
    }
    public List<umlMM_Class> getUmlmm_classs() {
        return umlmm_classs;
    }

    public void addUmlmm_class(Umlmm_class umlmm_class) {
        this.umlmm_classs.add(umlmm_class);
    }

}