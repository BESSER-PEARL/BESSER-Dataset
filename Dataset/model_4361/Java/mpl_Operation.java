





import java.util.List;
import java.util.ArrayList;

public class mpl_Operation extends FunctionalUnit {






    private mpl_MPLModel mpl_mplmodel;




    private mpl_OperationExpression mpl_operationexpression;


    public mpl_Operation(
    ) {
        super(
        );
    }



    public mpl_MPLModel getMpl_mplmodel() {
        return mpl_mplmodel;
    }

    public void setMpl_mplmodel(mpl_MPLModel mpl_mplmodel) {
        this.mpl_mplmodel = mpl_mplmodel;
    }
    public mpl_OperationExpression getMpl_operationexpression() {
        return mpl_operationexpression;
    }

    public void setMpl_operationexpression(mpl_OperationExpression mpl_operationexpression) {
        this.mpl_operationexpression = mpl_operationexpression;
    }

}