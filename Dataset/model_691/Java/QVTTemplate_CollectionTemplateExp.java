





import java.util.List;
import java.util.ArrayList;

public class QVTTemplate_CollectionTemplateExp extends TemplateExp {






    private CollectionType collectiontype;




    private Variable variable;




    private List<OclExpression> oclexpressions;


    public QVTTemplate_CollectionTemplateExp(
    ) {
        super(
        );
        this.oclexpressions = new ArrayList<>();
    }

    public QVTTemplate_CollectionTemplateExp(
        ArrayList<OclExpression> oclexpressions    ) {
        this.oclexpressions = oclexpressions;
    }


    public CollectionType getCollectiontype() {
        return collectiontype;
    }

    public void setCollectiontype(CollectionType collectiontype) {
        this.collectiontype = collectiontype;
    }
    public Variable getVariable() {
        return variable;
    }

    public void setVariable(Variable variable) {
        this.variable = variable;
    }
    public List<OclExpression> getOclexpressions() {
        return oclexpressions;
    }

    public void addOclexpression(Oclexpression oclexpression) {
        this.oclexpressions.add(oclexpression);
    }

}