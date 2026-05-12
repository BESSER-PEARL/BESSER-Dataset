





import java.util.List;
import java.util.ArrayList;

public class stateMachineActions_EXPRESSION  {

    private String operator;





    private stateMachineActions_TERM statemachineactions_term;




    private stateMachineActions_TERM statemachineactions_term;




    private stateMachineActions_Assignment statemachineactions_assignment;




    private stateMachineActions_TERM statemachineactions_term;


    public stateMachineActions_EXPRESSION(
        String operator    ) {
        this.operator = operator;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public stateMachineActions_TERM getStatemachineactions_term() {
        return statemachineactions_term;
    }

    public void setStatemachineactions_term(stateMachineActions_TERM statemachineactions_term) {
        this.statemachineactions_term = statemachineactions_term;
    }
    public stateMachineActions_TERM getStatemachineactions_term() {
        return statemachineactions_term;
    }

    public void setStatemachineactions_term(stateMachineActions_TERM statemachineactions_term) {
        this.statemachineactions_term = statemachineactions_term;
    }
    public stateMachineActions_Assignment getStatemachineactions_assignment() {
        return statemachineactions_assignment;
    }

    public void setStatemachineactions_assignment(stateMachineActions_Assignment statemachineactions_assignment) {
        this.statemachineactions_assignment = statemachineactions_assignment;
    }
    public stateMachineActions_TERM getStatemachineactions_term() {
        return statemachineactions_term;
    }

    public void setStatemachineactions_term(stateMachineActions_TERM statemachineactions_term) {
        this.statemachineactions_term = statemachineactions_term;
    }

}