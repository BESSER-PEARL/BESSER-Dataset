





import java.util.List;
import java.util.ArrayList;

public class FlatQVT_CollectionTemplateExp extends TemplateExp {






    private CollectionType collectiontype;




    private List<OclExpression> oclexpressions;


    public FlatQVT_CollectionTemplateExp(
    ) {
        super(
        );
        this.oclexpressions = new ArrayList<>();
    }

    public FlatQVT_CollectionTemplateExp(
        ArrayList<OclExpression> oclexpressions    ) {
        this.oclexpressions = oclexpressions;
    }


    public CollectionType getCollectiontype() {
        return collectiontype;
    }

    public void setCollectiontype(CollectionType collectiontype) {
        this.collectiontype = collectiontype;
    }
    public List<OclExpression> getOclexpressions() {
        return oclexpressions;
    }

    public void addOclexpression(Oclexpression oclexpression) {
        this.oclexpressions.add(oclexpression);
    }

}