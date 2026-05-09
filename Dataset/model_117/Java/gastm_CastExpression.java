





import java.util.List;
import java.util.ArrayList;

public class gastm_CastExpression extends Expression {






    private gastm_TypeReference gastm_typereference;




    private gastm_Expression gastm_expression;


    public gastm_CastExpression(
    ) {
        super(
        );
    }



    public gastm_TypeReference getGastm_typereference() {
        return gastm_typereference;
    }

    public void setGastm_typereference(gastm_TypeReference gastm_typereference) {
        this.gastm_typereference = gastm_typereference;
    }
    public gastm_Expression getGastm_expression() {
        return gastm_expression;
    }

    public void setGastm_expression(gastm_Expression gastm_expression) {
        this.gastm_expression = gastm_expression;
    }

}