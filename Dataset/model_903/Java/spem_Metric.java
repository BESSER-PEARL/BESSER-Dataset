





import java.util.List;
import java.util.ArrayList;

public class spem_Metric extends DescribableElement {

    private String expression;





    private spem_DescribableElement spem_describableelement;


    public spem_Metric(
        String expression    ) {
        super(
        );
        this.expression = expression;
    }


    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }

    public spem_DescribableElement getSpem_describableelement() {
        return spem_describableelement;
    }

    public void setSpem_describableelement(spem_DescribableElement spem_describableelement) {
        this.spem_describableelement = spem_describableelement;
    }

}