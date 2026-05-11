





import java.util.List;
import java.util.ArrayList;

public class simpleuml_Class extends Classifier {






    private List<simpleuml_Association> simpleuml_associations;




    private simpleuml_Association simpleuml_association;




    private List<simpleuml_Association> simpleuml_associations;




    private simpleuml_Association simpleuml_association;




    private List<simpleuml_Class> simpleuml_classs;




    private simpleuml_Class simpleuml_class;


    public simpleuml_Class(
    ) {
        super(
        );
        this.simpleuml_associations = new ArrayList<>();
        this.simpleuml_associations = new ArrayList<>();
        this.simpleuml_classs = new ArrayList<>();
    }

    public simpleuml_Class(
        ArrayList<simpleuml_Association> simpleuml_associations,        ArrayList<simpleuml_Association> simpleuml_associations,        ArrayList<simpleuml_Class> simpleuml_classs    ) {
        this.simpleuml_associations = simpleuml_associations;
        this.simpleuml_associations = simpleuml_associations;
        this.simpleuml_classs = simpleuml_classs;
    }


    public List<simpleuml_Association> getSimpleuml_associations() {
        return simpleuml_associations;
    }

    public void addSimpleuml_association(Simpleuml_association simpleuml_association) {
        this.simpleuml_associations.add(simpleuml_association);
    }
    public simpleuml_Association getSimpleuml_association() {
        return simpleuml_association;
    }

    public void setSimpleuml_association(simpleuml_Association simpleuml_association) {
        this.simpleuml_association = simpleuml_association;
    }
    public List<simpleuml_Association> getSimpleuml_associations() {
        return simpleuml_associations;
    }

    public void addSimpleuml_association(Simpleuml_association simpleuml_association) {
        this.simpleuml_associations.add(simpleuml_association);
    }
    public simpleuml_Association getSimpleuml_association() {
        return simpleuml_association;
    }

    public void setSimpleuml_association(simpleuml_Association simpleuml_association) {
        this.simpleuml_association = simpleuml_association;
    }
    public List<simpleuml_Class> getSimpleuml_classs() {
        return simpleuml_classs;
    }

    public void addSimpleuml_class(Simpleuml_class simpleuml_class) {
        this.simpleuml_classs.add(simpleuml_class);
    }
    public simpleuml_Class getSimpleuml_class() {
        return simpleuml_class;
    }

    public void setSimpleuml_class(simpleuml_Class simpleuml_class) {
        this.simpleuml_class = simpleuml_class;
    }

}