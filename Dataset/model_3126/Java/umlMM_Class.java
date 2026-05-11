





import java.util.List;
import java.util.ArrayList;

public class umlMM_Class extends Classifier {

    private String kind;





    private umlMM_Class umlmm_class;




    private umlMM_Class umlmm_class;




    private List<umlMM_Association> umlmm_associations;




    private List<umlMM_Association> umlmm_associations;




    private umlMM_Association umlmm_association;




    private umlMM_Association umlmm_association;


    public umlMM_Class(
        String kind    ) {
        super(
        );
        this.kind = kind;
        this.umlmm_associations = new ArrayList<>();
        this.umlmm_associations = new ArrayList<>();
    }

    public umlMM_Class(
        String kind        ArrayList<umlMM_Association> umlmm_associations,        ArrayList<umlMM_Association> umlmm_associations    ) {
        this.kind = kind;
        this.umlmm_associations = umlmm_associations;
        this.umlmm_associations = umlmm_associations;
    }

    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public umlMM_Class getUmlmm_class() {
        return umlmm_class;
    }

    public void setUmlmm_class(umlMM_Class umlmm_class) {
        this.umlmm_class = umlmm_class;
    }
    public umlMM_Class getUmlmm_class() {
        return umlmm_class;
    }

    public void setUmlmm_class(umlMM_Class umlmm_class) {
        this.umlmm_class = umlmm_class;
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

}