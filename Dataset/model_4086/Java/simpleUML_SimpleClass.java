





import java.util.List;
import java.util.ArrayList;

public class simpleUML_SimpleClass  {

    private String simpleName;





    private List<simpleUML_SimpleClass> simpleuml_simpleclasss;




    private simpleUML_Model simpleuml_model;


    public simpleUML_SimpleClass(
        String simpleName    ) {
        this.simpleName = simpleName;
        this.simpleuml_simpleclasss = new ArrayList<>();
    }

    public simpleUML_SimpleClass(
        String simpleName        ArrayList<simpleUML_SimpleClass> simpleuml_simpleclasss    ) {
        this.simpleName = simpleName;
        this.simpleuml_simpleclasss = simpleuml_simpleclasss;
    }

    public String getSimplename() {
        return simpleName;
    }

    public void setSimplename(String simpleName) {
        this.simpleName = simpleName;
    }

    public List<simpleUML_SimpleClass> getSimpleuml_simpleclasss() {
        return simpleuml_simpleclasss;
    }

    public void addSimpleuml_simpleclass(Simpleuml_simpleclass simpleuml_simpleclass) {
        this.simpleuml_simpleclasss.add(simpleuml_simpleclass);
    }
    public simpleUML_Model getSimpleuml_model() {
        return simpleuml_model;
    }

    public void setSimpleuml_model(simpleUML_Model simpleuml_model) {
        this.simpleuml_model = simpleuml_model;
    }

}