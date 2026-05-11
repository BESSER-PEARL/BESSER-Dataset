





import java.util.List;
import java.util.ArrayList;

public class SPL_ForwardExp extends Expression {

    private boolean isParallel;





    private SPL_Expression spl_expression;


    public SPL_ForwardExp(
        boolean isParallel    ) {
        super(
        );
        this.isParallel = isParallel;
    }


    public boolean getIsparallel() {
        return isParallel;
    }

    public void setIsparallel(boolean isParallel) {
        this.isParallel = isParallel;
    }

    public SPL_Expression getSpl_expression() {
        return spl_expression;
    }

    public void setSpl_expression(SPL_Expression spl_expression) {
        this.spl_expression = spl_expression;
    }

}