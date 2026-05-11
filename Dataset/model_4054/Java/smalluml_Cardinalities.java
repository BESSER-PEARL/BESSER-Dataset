





import java.util.List;
import java.util.ArrayList;

public class smalluml_Cardinalities  {

    private int lowerbound;
    private int upperbound;



    public smalluml_Cardinalities(
        int lowerbound,        int upperbound    ) {
        this.lowerbound = lowerbound;
        this.upperbound = upperbound;
    }


    public int getLowerbound() {
        return lowerbound;
    }

    public void setLowerbound(int lowerbound) {
        this.lowerbound = lowerbound;
    }
    public int getUpperbound() {
        return upperbound;
    }

    public void setUpperbound(int upperbound) {
        this.upperbound = upperbound;
    }


}