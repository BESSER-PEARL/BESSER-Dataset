





import java.util.List;
import java.util.ArrayList;

public class atlstatic_OCL_LoopExp extends PropertyCallExp {






    private List<Iterator> iterators;




    private OclExpression oclexpression;


    public atlstatic_OCL_LoopExp(
    ) {
        super(
        );
        this.iterators = new ArrayList<>();
    }

    public atlstatic_OCL_LoopExp(
        ArrayList<Iterator> iterators    ) {
        this.iterators = iterators;
    }


    public List<Iterator> getIterators() {
        return iterators;
    }

    public void addIterator(Iterator iterator) {
        this.iterators.add(iterator);
    }
    public OclExpression getOclexpression() {
        return oclexpression;
    }

    public void setOclexpression(OclExpression oclexpression) {
        this.oclexpression = oclexpression;
    }

}