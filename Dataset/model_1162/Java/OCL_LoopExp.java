





import java.util.List;
import java.util.ArrayList;

public class OCL_LoopExp extends PropertyCallExp {






    private OclExpression oclexpression;




    private List<Iterator> iterators;


    public OCL_LoopExp(
    ) {
        super(
        );
        this.iterators = new ArrayList<>();
    }

    public OCL_LoopExp(
        ArrayList<Iterator> iterators    ) {
        this.iterators = iterators;
    }


    public OclExpression getOclexpression() {
        return oclexpression;
    }

    public void setOclexpression(OclExpression oclexpression) {
        this.oclexpression = oclexpression;
    }
    public List<Iterator> getIterators() {
        return iterators;
    }

    public void addIterator(Iterator iterator) {
        this.iterators.add(iterator);
    }

}