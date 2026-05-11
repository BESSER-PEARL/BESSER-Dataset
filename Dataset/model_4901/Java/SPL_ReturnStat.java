





import java.util.List;
import java.util.ArrayList;

public class SPL_ReturnStat extends Statement {






    private SPL_Expression spl_expression;




    private SPL_NamedBranch spl_namedbranch;


    public SPL_ReturnStat(
    ) {
        super(
        );
    }



    public SPL_Expression getSpl_expression() {
        return spl_expression;
    }

    public void setSpl_expression(SPL_Expression spl_expression) {
        this.spl_expression = spl_expression;
    }
    public SPL_NamedBranch getSpl_namedbranch() {
        return spl_namedbranch;
    }

    public void setSpl_namedbranch(SPL_NamedBranch spl_namedbranch) {
        this.spl_namedbranch = spl_namedbranch;
    }

}