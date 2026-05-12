





import java.util.List;
import java.util.ArrayList;

public class IExpressionTerm  {






    private model_expression_Operation model_expression_operation;




    private model_component_Port model_component_port;




    private model_state_DataStateVariable model_state_datastatevariable;


    public IExpressionTerm(
    ) {
    }



    public model_expression_Operation getModel_expression_operation() {
        return model_expression_operation;
    }

    public void setModel_expression_operation(model_expression_Operation model_expression_operation) {
        this.model_expression_operation = model_expression_operation;
    }
    public model_component_Port getModel_component_port() {
        return model_component_port;
    }

    public void setModel_component_port(model_component_Port model_component_port) {
        this.model_component_port = model_component_port;
    }
    public model_state_DataStateVariable getModel_state_datastatevariable() {
        return model_state_datastatevariable;
    }

    public void setModel_state_datastatevariable(model_state_DataStateVariable model_state_datastatevariable) {
        this.model_state_datastatevariable = model_state_datastatevariable;
    }

}