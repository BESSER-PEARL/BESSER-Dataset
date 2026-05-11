





import java.util.List;
import java.util.ArrayList;

public class wsmodel3_Function  {

    private String expression;





    private wsmodel3_Orchestrator wsmodel3_orchestrator;




    private wsmodel3_InputOrchestrator wsmodel3_inputorchestrator;




    private List<wsmodel3_Break> wsmodel3_breaks;


    public wsmodel3_Function(
        String expression    ) {
        this.expression = expression;
        this.wsmodel3_breaks = new ArrayList<>();
    }

    public wsmodel3_Function(
        String expression        ArrayList<wsmodel3_Break> wsmodel3_breaks    ) {
        this.expression = expression;
        this.wsmodel3_breaks = wsmodel3_breaks;
    }

    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }

    public wsmodel3_Orchestrator getWsmodel3_orchestrator() {
        return wsmodel3_orchestrator;
    }

    public void setWsmodel3_orchestrator(wsmodel3_Orchestrator wsmodel3_orchestrator) {
        this.wsmodel3_orchestrator = wsmodel3_orchestrator;
    }
    public wsmodel3_InputOrchestrator getWsmodel3_inputorchestrator() {
        return wsmodel3_inputorchestrator;
    }

    public void setWsmodel3_inputorchestrator(wsmodel3_InputOrchestrator wsmodel3_inputorchestrator) {
        this.wsmodel3_inputorchestrator = wsmodel3_inputorchestrator;
    }
    public List<wsmodel3_Break> getWsmodel3_breaks() {
        return wsmodel3_breaks;
    }

    public void addWsmodel3_break(Wsmodel3_break wsmodel3_break) {
        this.wsmodel3_breaks.add(wsmodel3_break);
    }

}