





import java.util.List;
import java.util.ArrayList;

public class sequence_template_TLifelineMapping extends template_TMessageExtremity, template_TAbstractMapping {

    private String eolVisibleExpression;



    public sequence_template_TLifelineMapping(
        String eolVisibleExpression    ) {
        super(
        );
        this.eolVisibleExpression = eolVisibleExpression;
    }


    public String getEolvisibleexpression() {
        return eolVisibleExpression;
    }

    public void setEolvisibleexpression(String eolVisibleExpression) {
        this.eolVisibleExpression = eolVisibleExpression;
    }


}