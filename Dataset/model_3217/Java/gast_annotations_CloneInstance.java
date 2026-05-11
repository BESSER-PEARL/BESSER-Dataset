





import java.util.List;
import java.util.ArrayList;

public class gast_annotations_CloneInstance extends core_ModelElement, annotations_ModelAnnotation {






    private Clone clone;




    private List<Statement> statements;


    public gast_annotations_CloneInstance(
    ) {
        super(
        );
        this.statements = new ArrayList<>();
    }

    public gast_annotations_CloneInstance(
        ArrayList<Statement> statements    ) {
        this.statements = statements;
    }


    public Clone getClone() {
        return clone;
    }

    public void setClone(Clone clone) {
        this.clone = clone;
    }
    public List<Statement> getStatements() {
        return statements;
    }

    public void addStatement(Statement statement) {
        this.statements.add(statement);
    }

}