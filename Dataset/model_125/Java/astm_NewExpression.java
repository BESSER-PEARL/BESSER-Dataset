





import java.util.List;
import java.util.ArrayList;

public class astm_NewExpression extends Expression {






    private List<OtherSyntaxObject> othersyntaxobjects;




    private TypeReference typereference;


    public astm_NewExpression(
    ) {
        super(
        );
        this.othersyntaxobjects = new ArrayList<>();
    }

    public astm_NewExpression(
        ArrayList<OtherSyntaxObject> othersyntaxobjects    ) {
        this.othersyntaxobjects = othersyntaxobjects;
    }


    public List<OtherSyntaxObject> getOthersyntaxobjects() {
        return othersyntaxobjects;
    }

    public void addOthersyntaxobject(Othersyntaxobject othersyntaxobject) {
        this.othersyntaxobjects.add(othersyntaxobject);
    }
    public TypeReference getTypereference() {
        return typereference;
    }

    public void setTypereference(TypeReference typereference) {
        this.typereference = typereference;
    }

}