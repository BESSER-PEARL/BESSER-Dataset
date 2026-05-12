





import java.util.List;
import java.util.ArrayList;

public class jDOQL_ResultClause  {

    private boolean isDistinct;



    public jDOQL_ResultClause(
        boolean isDistinct    ) {
        this.isDistinct = isDistinct;
    }


    public boolean getIsdistinct() {
        return isDistinct;
    }

    public void setIsdistinct(boolean isDistinct) {
        this.isDistinct = isDistinct;
    }


}