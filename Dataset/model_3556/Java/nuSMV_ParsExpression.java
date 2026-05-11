





import java.util.List;
import java.util.ArrayList;

public class nuSMV_ParsExpression extends SimpleExpression {

    private boolean isNext;





    private nuSMV_SimpleExpression nusmv_simpleexpression;


    public nuSMV_ParsExpression(
        boolean isNext    ) {
        super(
        );
        this.isNext = isNext;
    }


    public boolean getIsnext() {
        return isNext;
    }

    public void setIsnext(boolean isNext) {
        this.isNext = isNext;
    }

    public nuSMV_SimpleExpression getNusmv_simpleexpression() {
        return nusmv_simpleexpression;
    }

    public void setNusmv_simpleexpression(nuSMV_SimpleExpression nusmv_simpleexpression) {
        this.nusmv_simpleexpression = nusmv_simpleexpression;
    }

}