





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_ProtocolStateMachine extends StateMachine {






    private CompleteDSLPckg_ProtocolConformance completedslpckg_protocolconformance;




    private List<CompleteDSLPckg_ProtocolConformance> completedslpckg_protocolconformances;




    private CompleteDSLPckg_ProtocolConformance completedslpckg_protocolconformance;


    public CompleteDSLPckg_ProtocolStateMachine(
    ) {
        super(
        );
        this.completedslpckg_protocolconformances = new ArrayList<>();
    }

    public CompleteDSLPckg_ProtocolStateMachine(
        ArrayList<CompleteDSLPckg_ProtocolConformance> completedslpckg_protocolconformances    ) {
        this.completedslpckg_protocolconformances = completedslpckg_protocolconformances;
    }


    public CompleteDSLPckg_ProtocolConformance getCompletedslpckg_protocolconformance() {
        return completedslpckg_protocolconformance;
    }

    public void setCompletedslpckg_protocolconformance(CompleteDSLPckg_ProtocolConformance completedslpckg_protocolconformance) {
        this.completedslpckg_protocolconformance = completedslpckg_protocolconformance;
    }
    public List<CompleteDSLPckg_ProtocolConformance> getCompletedslpckg_protocolconformances() {
        return completedslpckg_protocolconformances;
    }

    public void addCompletedslpckg_protocolconformance(Completedslpckg_protocolconformance completedslpckg_protocolconformance) {
        this.completedslpckg_protocolconformances.add(completedslpckg_protocolconformance);
    }
    public CompleteDSLPckg_ProtocolConformance getCompletedslpckg_protocolconformance() {
        return completedslpckg_protocolconformance;
    }

    public void setCompletedslpckg_protocolconformance(CompleteDSLPckg_ProtocolConformance completedslpckg_protocolconformance) {
        this.completedslpckg_protocolconformance = completedslpckg_protocolconformance;
    }

}