





import java.util.List;
import java.util.ArrayList;

public class simpleuml_Class extends Classifier {






    private simpleuml_Class simpleuml_class;




    private List<simpleuml_Class> simpleuml_classs;


    public simpleuml_Class(
    ) {
        super(
        );
        this.simpleuml_classs = new ArrayList<>();
    }

    public simpleuml_Class(
        ArrayList<simpleuml_Class> simpleuml_classs    ) {
        this.simpleuml_classs = simpleuml_classs;
    }


    public simpleuml_Class getSimpleuml_class() {
        return simpleuml_class;
    }

    public void setSimpleuml_class(simpleuml_Class simpleuml_class) {
        this.simpleuml_class = simpleuml_class;
    }
    public List<simpleuml_Class> getSimpleuml_classs() {
        return simpleuml_classs;
    }

    public void addSimpleuml_class(Simpleuml_class simpleuml_class) {
        this.simpleuml_classs.add(simpleuml_class);
    }

}