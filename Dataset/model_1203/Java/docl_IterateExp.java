





import java.util.List;
import java.util.ArrayList;

public class docl_IterateExp extends OclExpression {






    private docl_LocalVariable docl_localvariable;




    private docl_OclExpression docl_oclexpression;




    private List<docl_Iterator> docl_iterators;


    public docl_IterateExp(
    ) {
        super(
        );
        this.docl_iterators = new ArrayList<>();
    }

    public docl_IterateExp(
        ArrayList<docl_Iterator> docl_iterators    ) {
        this.docl_iterators = docl_iterators;
    }


    public docl_LocalVariable getDocl_localvariable() {
        return docl_localvariable;
    }

    public void setDocl_localvariable(docl_LocalVariable docl_localvariable) {
        this.docl_localvariable = docl_localvariable;
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