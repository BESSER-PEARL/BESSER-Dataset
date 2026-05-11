





import java.util.List;
import java.util.ArrayList;

public class nuSMV_SetExpression extends SimpleExpression {






    private List<nuSMV_SimpleExpression> nusmv_simpleexpressions;


    public nuSMV_SetExpression(
    ) {
        super(
        );
        this.nusmv_simpleexpressions = new ArrayList<>();
    }

    public nuSMV_SetExpression(
        ArrayList<nuSMV_SimpleExpression> nusmv_simpleexpressions    ) {
        this.nusmv_simpleexpressions = nusmv_simpleexpressions;
    }


    public List<nuSMV_SimpleExpression> getNusmv_simpleexpressions() {
        return nusmv_simpleexpressions;
    }

    public void addNusmv_simpleexpression(Nusmv_simpleexpression nusmv_simpleexpression) {
        this.nusmv_simpleexpressions.add(nusmv_simpleexpression);
    }

}