





import java.util.List;
import java.util.ArrayList;

public class SOS_adtmm_CTerm extends Term {

    private int iter;





    private Operation operation;


    public SOS_adtmm_CTerm(
        int iter    ) {
        super(
        );
        this.iter = iter;
    }


    public int getIter() {
        return iter;
    }

    public void setIter(int iter) {
        this.iter = iter;
    }

    public Operation getOperation() {
        return operation;
    }

    public void setOperation(Operation operation) {
        this.operation = operation;
    }

}