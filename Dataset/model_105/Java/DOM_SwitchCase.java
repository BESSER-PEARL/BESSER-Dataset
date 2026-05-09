





import java.util.List;
import java.util.ArrayList;

public class DOM_SwitchCase extends Statement {

    private String default;





    private DOM_Expression dom_expression;


    public DOM_SwitchCase(
        String default    ) {
        super(
        );
        this.default = default;
    }


    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }

    public DOM_Expression getDom_expression() {
        return dom_expression;
    }

    public void setDom_expression(DOM_Expression dom_expression) {
        this.dom_expression = dom_expression;
    }

}