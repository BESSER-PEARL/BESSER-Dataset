





import java.util.List;
import java.util.ArrayList;

public class wsmodel3_OutputOrchestrator  {






    private List<wsmodel3_InputOrchestrator> wsmodel3_inputorchestrators;




    private List<wsmodel3_ExternalAPI> wsmodel3_externalapis;




    private wsmodel3_InputBridge wsmodel3_inputbridge;




    private wsmodel3_Function wsmodel3_function;




    private wsmodel3_Orchestrator wsmodel3_orchestrator;




    private List<wsmodel3_REST> wsmodel3_rests;




    private List<wsmodel3_OrchestratorData> wsmodel3_orchestratordatas;


    public wsmodel3_OutputOrchestrator(
    ) {
        this.wsmodel3_inputorchestrators = new ArrayList<>();
        this.wsmodel3_externalapis = new ArrayList<>();
        this.wsmodel3_rests = new ArrayList<>();
        this.wsmodel3_orchestratordatas = new ArrayList<>();
    }

    public wsmodel3_OutputOrchestrator(
        ArrayList<wsmodel3_InputOrchestrator> wsmodel3_inputorchestrators,        ArrayList<wsmodel3_ExternalAPI> wsmodel3_externalapis,        ArrayList<wsmodel3_REST> wsmodel3_rests,        ArrayList<wsmodel3_OrchestratorData> wsmodel3_orchestratordatas    ) {
        this.wsmodel3_inputorchestrators = wsmodel3_inputorchestrators;
        this.wsmodel3_externalapis = wsmodel3_externalapis;
        this.wsmodel3_rests = wsmodel3_rests;
        this.wsmodel3_orchestratordatas = wsmodel3_orchestratordatas;
    }


    public List<wsmodel3_InputOrchestrator> getWsmodel3_inputorchestrators() {
        return wsmodel3_inputorchestrators;
    }

    public void addWsmodel3_inputorchestrator(Wsmodel3_inputorchestrator wsmodel3_inputorchestrator) {
        this.wsmodel3_inputorchestrators.add(wsmodel3_inputorchestrator);
    }
    public List<wsmodel3_ExternalAPI> getWsmodel3_externalapis() {
        return wsmodel3_externalapis;
    }

    public void addWsmodel3_externalapi(Wsmodel3_externalapi wsmodel3_externalapi) {
        this.wsmodel3_externalapis.add(wsmodel3_externalapi);
    }
    public wsmodel3_InputBridge getWsmodel3_inputbridge() {
        return wsmodel3_inputbridge;
    }

    public void setWsmodel3_inputbridge(wsmodel3_InputBridge wsmodel3_inputbridge) {
        this.wsmodel3_inputbridge = wsmodel3_inputbridge;
    }
    public wsmodel3_Function getWsmodel3_function() {
        return wsmodel3_function;
    }

    public void setWsmodel3_function(wsmodel3_Function wsmodel3_function) {
        this.wsmodel3_function = wsmodel3_function;
    }
    public wsmodel3_Orchestrator getWsmodel3_orchestrator() {
        return wsmodel3_orchestrator;
    }

    public void setWsmodel3_orchestrator(wsmodel3_Orchestrator wsmodel3_orchestrator) {
        this.wsmodel3_orchestrator = wsmodel3_orchestrator;
    }
    public List<wsmodel3_REST> getWsmodel3_rests() {
        return wsmodel3_rests;
    }

    public void addWsmodel3_rest(Wsmodel3_rest wsmodel3_rest) {
        this.wsmodel3_rests.add(wsmodel3_rest);
    }
    public List<wsmodel3_OrchestratorData> getWsmodel3_orchestratordatas() {
        return wsmodel3_orchestratordatas;
    }

    public void addWsmodel3_orchestratordata(Wsmodel3_orchestratordata wsmodel3_orchestratordata) {
        this.wsmodel3_orchestratordatas.add(wsmodel3_orchestratordata);
    }

}