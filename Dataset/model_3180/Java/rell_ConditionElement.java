





import java.util.List;
import java.util.ArrayList;

public class rell_ConditionElement  {

    private String compareName;





    private rell_Expression rell_expression;


    public rell_ConditionElement(
        String compareName    ) {
        this.compareName = compareName;
    }


    public String getComparename() {
        return compareName;
    }

    public void setComparename(String compareName) {
        this.compareName = compareName;
    }

    public rell_Expression getRell_expression() {
        return rell_expression;
    }

    public void setRell_expression(rell_Expression rell_expression) {
        this.rell_expression = rell_expression;
    }

}