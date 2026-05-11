





import java.util.List;
import java.util.ArrayList;

public class siddhi_MathLogicalOperation extends MathOperation {






    private siddhi_AND siddhi_and;




    private siddhi_MathOperation siddhi_mathoperation;


    public siddhi_MathLogicalOperation(
    ) {
        super(
        );
    }



    public siddhi_AND getSiddhi_and() {
        return siddhi_and;
    }

    public void setSiddhi_and(siddhi_AND siddhi_and) {
        this.siddhi_and = siddhi_and;
    }
    public siddhi_MathOperation getSiddhi_mathoperation() {
        return siddhi_mathoperation;
    }

    public void setSiddhi_mathoperation(siddhi_MathOperation siddhi_mathoperation) {
        this.siddhi_mathoperation = siddhi_mathoperation;
    }

}