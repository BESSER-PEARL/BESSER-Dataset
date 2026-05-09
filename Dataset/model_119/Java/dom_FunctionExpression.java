





import java.util.List;
import java.util.ArrayList;

public class dom_FunctionExpression extends Expression {

    private int parametersPosition;





    private dom_Identifier dom_identifier;




    private dom_Comment dom_comment;




    private List<dom_Parameter> dom_parameters;


    public dom_FunctionExpression(
        int parametersPosition    ) {
        super(
        );
        this.parametersPosition = parametersPosition;
        this.dom_parameters = new ArrayList<>();
    }

    public dom_FunctionExpression(
        int parametersPosition        ArrayList<dom_Parameter> dom_parameters    ) {
        this.parametersPosition = parametersPosition;
        this.dom_parameters = dom_parameters;
    }

    public int getParametersposition() {
        return parametersPosition;
    }

    public void setParametersposition(int parametersPosition) {
        this.parametersPosition = parametersPosition;
    }

    public dom_Identifier getDom_identifier() {
        return dom_identifier;
    }

    public void setDom_identifier(dom_Identifier dom_identifier) {
        this.dom_identifier = dom_identifier;
    }
    public dom_Comment getDom_comment() {
        return dom_comment;
    }

    public void setDom_comment(dom_Comment dom_comment) {
        this.dom_comment = dom_comment;
    }
    public List<dom_Parameter> getDom_parameters() {
        return dom_parameters;
    }

    public void addDom_parameter(Dom_parameter dom_parameter) {
        this.dom_parameters.add(dom_parameter);
    }

}