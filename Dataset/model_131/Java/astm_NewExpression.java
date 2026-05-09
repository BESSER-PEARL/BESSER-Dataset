





import java.util.List;
import java.util.ArrayList;

public class astm_NewExpression extends Expression {






    private astm_TypeReference astm_typereference;




    private List<astm_OtherSyntaxObject> astm_othersyntaxobjects;


    public astm_NewExpression(
    ) {
        super(
        );
        this.astm_othersyntaxobjects = new ArrayList<>();
    }

    public astm_NewExpression(
        ArrayList<astm_OtherSyntaxObject> astm_othersyntaxobjects    ) {
        this.astm_othersyntaxobjects = astm_othersyntaxobjects;
    }


    public astm_TypeReference getAstm_typereference() {
        return astm_typereference;
    }

    public void setAstm_typereference(astm_TypeReference astm_typereference) {
        this.astm_typereference = astm_typereference;
    }
    public List<astm_OtherSyntaxObject> getAstm_othersyntaxobjects() {
        return astm_othersyntaxobjects;
    }

    public void addAstm_othersyntaxobject(Astm_othersyntaxobject astm_othersyntaxobject) {
        this.astm_othersyntaxobjects.add(astm_othersyntaxobject);
    }

}