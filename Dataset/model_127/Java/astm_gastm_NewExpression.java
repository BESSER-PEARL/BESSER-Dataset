





import java.util.List;
import java.util.ArrayList;

public class astm_gastm_NewExpression extends Expression {






    private TypeReference typereference;




    private List<OtherSyntaxObject> othersyntaxobjects;


    public astm_gastm_NewExpression(
    ) {
        super(
        );
        this.othersyntaxobjects = new ArrayList<>();
    }

    public astm_gastm_NewExpression(
        ArrayList<OtherSyntaxObject> othersyntaxobjects    ) {
        this.othersyntaxobjects = othersyntaxobjects;
    }


    public TypeReference getTypereference() {
        return typereference;
    }

    public void setTypereference(TypeReference typereference) {
        this.typereference = typereference;
    }
    public List<OtherSyntaxObject> getOthersyntaxobjects() {
        return othersyntaxobjects;
    }

    public void addOthersyntaxobject(Othersyntaxobject othersyntaxobject) {
        this.othersyntaxobjects.add(othersyntaxobject);
    }

}