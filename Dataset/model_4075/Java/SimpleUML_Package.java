





import java.util.List;
import java.util.ArrayList;

public class SimpleUML_Package extends NamedElement {






    private List<SimpleUML_Class> simpleuml_classs;


    public SimpleUML_Package(
    ) {
        super(
        );
        this.simpleuml_classs = new ArrayList<>();
    }

    public SimpleUML_Package(
        ArrayList<SimpleUML_Class> simpleuml_classs    ) {
        this.simpleuml_classs = simpleuml_classs;
    }


    public List<SimpleUML_Class> getSimpleuml_classs() {
        return simpleuml_classs;
    }

    public void addSimpleuml_class(Simpleuml_class simpleuml_class) {
        this.simpleuml_classs.add(simpleuml_class);
    }

}