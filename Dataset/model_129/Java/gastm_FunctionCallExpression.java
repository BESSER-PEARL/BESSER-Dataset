





import java.util.List;
import java.util.ArrayList;

public class gastm_FunctionCallExpression extends Expression {






    private List<OtherSyntaxObject> othersyntaxobjects;


    public gastm_FunctionCallExpression(
    ) {
        super(
        );
        this.othersyntaxobjects = new ArrayList<>();
    }

    public gastm_FunctionCallExpression(
        ArrayList<OtherSyntaxObject> othersyntaxobjects    ) {
        this.othersyntaxobjects = othersyntaxobjects;
    }


    public List<OtherSyntaxObject> getOthersyntaxobjects() {
        return othersyntaxobjects;
    }

    public void addOthersyntaxobject(Othersyntaxobject othersyntaxobject) {
        this.othersyntaxobjects.add(othersyntaxobject);
    }

}