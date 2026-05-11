





import java.util.List;
import java.util.ArrayList;

public class simpleuml_UMLClass extends Classifier {

    private String kind;





    private List<simpleuml_UMLClass> simpleuml_umlclasss;


    public simpleuml_UMLClass(
        String kind    ) {
        super(
        );
        this.kind = kind;
        this.simpleuml_umlclasss = new ArrayList<>();
    }

    public simpleuml_UMLClass(
        String kind        ArrayList<simpleuml_UMLClass> simpleuml_umlclasss    ) {
        this.kind = kind;
        this.simpleuml_umlclasss = simpleuml_umlclasss;
    }

    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public List<simpleuml_UMLClass> getSimpleuml_umlclasss() {
        return simpleuml_umlclasss;
    }

    public void addSimpleuml_umlclass(Simpleuml_umlclass simpleuml_umlclass) {
        this.simpleuml_umlclasss.add(simpleuml_umlclass);
    }

}