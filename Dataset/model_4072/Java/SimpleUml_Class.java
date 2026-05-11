





import java.util.List;
import java.util.ArrayList;

public class SimpleUml_Class extends NamedElement {






    private List<SimpleUml_Class> simpleuml_classs;


    public SimpleUml_Class(
    ) {
        super(
        );
        this.simpleuml_classs = new ArrayList<>();
    }

    public SimpleUml_Class(
        ArrayList<SimpleUml_Class> simpleuml_classs    ) {
        this.simpleuml_classs = simpleuml_classs;
    }


    public List<SimpleUml_Class> getSimpleuml_classs() {
        return simpleuml_classs;
    }

    public void addSimpleuml_class(Simpleuml_class simpleuml_class) {
        this.simpleuml_classs.add(simpleuml_class);
    }

}