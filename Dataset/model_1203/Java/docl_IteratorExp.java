





import java.util.List;
import java.util.ArrayList;

public class docl_IteratorExp extends OclExpression {






    private docl_OclExpression docl_oclexpression;




    private List<docl_Iterator> docl_iterators;


    public docl_IteratorExp(
    ) {
        super(
        );
        this.docl_iterators = new ArrayList<>();
    }

    public docl_IteratorExp(
        ArrayList<docl_Iterator> docl_iterators    ) {
        this.docl_iterators = docl_iterators;
    }


    public docl_OclExpression getDocl_oclexpression() {
        return docl_oclexpression;
    }

    public void setDocl_oclexpression(docl_OclExpression docl_oclexpression) {
        this.docl_oclexpression = docl_oclexpression;
    }
    public List<docl_Iterator> getDocl_iterators() {
        return docl_iterators;
    }

    public void addDocl_iterator(Docl_iterator docl_iterator) {
        this.docl_iterators.add(docl_iterator);
    }

}