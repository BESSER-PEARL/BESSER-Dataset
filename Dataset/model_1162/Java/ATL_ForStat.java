





import java.util.List;
import java.util.ArrayList;

public class ATL_ForStat extends Statement {






    private OclExpression oclexpression;




    private Iterator iterator;


    public ATL_ForStat(
    ) {
        super(
        );
    }



    public OclExpression getOclexpression() {
        return oclexpression;
    }

    public void setOclexpression(OclExpression oclexpression) {
        this.oclexpression = oclexpression;
    }
    public Iterator getIterator() {
        return iterator;
    }

    public void setIterator(Iterator iterator) {
        this.iterator = iterator;
    }

}