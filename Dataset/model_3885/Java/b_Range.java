





import java.util.List;
import java.util.ArrayList;

public class b_Range  {

    private int lowerBound;





    private b_Variable b_variable;


    public b_Range(
        int lowerBound    ) {
        this.lowerBound = lowerBound;
    }


    public int getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(int lowerBound) {
        this.lowerBound = lowerBound;
    }

    public b_Variable getB_variable() {
        return b_variable;
    }

    public void setB_variable(b_Variable b_variable) {
        this.b_variable = b_variable;
    }

}