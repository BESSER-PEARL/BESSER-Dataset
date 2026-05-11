





import java.util.List;
import java.util.ArrayList;

public class ale_Collection  {

    private int max;
    private int min;





    private ale_ForEach ale_foreach;




    private ale_ExpressionStmt ale_expressionstmt;


    public ale_Collection(
        int max,        int min    ) {
        this.max = max;
        this.min = min;
    }


    public int getMax() {
        return max;
    }

    public void setMax(int max) {
        this.max = max;
    }
    public int getMin() {
        return min;
    }

    public void setMin(int min) {
        this.min = min;
    }

    public ale_ForEach getAle_foreach() {
        return ale_foreach;
    }

    public void setAle_foreach(ale_ForEach ale_foreach) {
        this.ale_foreach = ale_foreach;
    }
    public ale_ExpressionStmt getAle_expressionstmt() {
        return ale_expressionstmt;
    }

    public void setAle_expressionstmt(ale_ExpressionStmt ale_expressionstmt) {
        this.ale_expressionstmt = ale_expressionstmt;
    }

}