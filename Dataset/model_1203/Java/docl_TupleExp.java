





import java.util.List;
import java.util.ArrayList;

public class docl_TupleExp extends OclExpression {






    private List<docl_TuplePart> docl_tupleparts;


    public docl_TupleExp(
    ) {
        super(
        );
        this.docl_tupleparts = new ArrayList<>();
    }

    public docl_TupleExp(
        ArrayList<docl_TuplePart> docl_tupleparts    ) {
        this.docl_tupleparts = docl_tupleparts;
    }


    public List<docl_TuplePart> getDocl_tupleparts() {
        return docl_tupleparts;
    }

    public void addDocl_tuplepart(Docl_tuplepart docl_tuplepart) {
        this.docl_tupleparts.add(docl_tuplepart);
    }

}