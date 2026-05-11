





import java.util.List;
import java.util.ArrayList;

public class nuSMV_UnaryFunctionExpression extends SimpleExpression {

    private String function;





    private nuSMV_SimpleExpression nusmv_simpleexpression;


    public nuSMV_UnaryFunctionExpression(
        String function    ) {
        super(
        );
        this.function = function;
    }


    public String getFunction() {
        return function;
    }

    public void setFunction(String function) {
        this.function = function;
    }

    public nuSMV_SimpleExpression getNusmv_simpleexpression() {
        return nusmv_simpleexpression;
    }

    public void setNusmv_simpleexpression(nuSMV_SimpleExpression nusmv_simpleexpression) {
        this.nusmv_simpleexpression = nusmv_simpleexpression;
    }

}