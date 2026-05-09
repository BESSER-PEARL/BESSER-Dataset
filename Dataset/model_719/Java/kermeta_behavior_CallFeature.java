





import java.util.List;
import java.util.ArrayList;

public class kermeta_behavior_CallFeature extends CallExpression {

    private String isAtpre;





    private behavior_Expression behavior_expression;


    public kermeta_behavior_CallFeature(
        String isAtpre    ) {
        super(
        );
        this.isAtpre = isAtpre;
    }


    public String getIsatpre() {
        return isAtpre;
    }

    public void setIsatpre(String isAtpre) {
        this.isAtpre = isAtpre;
    }

    public behavior_Expression getBehavior_expression() {
        return behavior_expression;
    }

    public void setBehavior_expression(behavior_Expression behavior_expression) {
        this.behavior_expression = behavior_expression;
    }

}