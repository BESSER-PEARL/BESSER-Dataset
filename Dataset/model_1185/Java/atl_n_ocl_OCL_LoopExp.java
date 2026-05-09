





import java.util.List;
import java.util.ArrayList;

public class atl_n_ocl_OCL_LoopExp extends PropertyCallExp {






    private List<Iterator> iterators;




    private OclExpression oclexpression;


    public atl_n_ocl_OCL_LoopExp(
    ) {
        super(
        );
        this.iterators = new ArrayList<>();
    }

    public atl_n_ocl_OCL_LoopExp(
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