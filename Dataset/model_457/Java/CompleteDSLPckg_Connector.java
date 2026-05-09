





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_Connector extends Feature {

    private String kind;





    private CompleteDSLPckg_Message completedslpckg_message;




    private CompleteDSLPckg_Connector completedslpckg_connector;




    private List<CompleteDSLPckg_Behavior> completedslpckg_behaviors;


    public CompleteDSLPckg_Connector(
        String kind    ) {
        super(
        );
        this.kind = kind;
        this.completedslpckg_behaviors = new ArrayList<>();
    }

    public CompleteDSLPckg_Connector(
        String kind        ArrayList<CompleteDSLPckg_Behavior> completedslpckg_behaviors    ) {
        this.kind = kind;
        this.completedslpckg_behaviors = completedslpckg_behaviors;
    }

    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public CompleteDSLPckg_Message getCompletedslpckg_message() {
        return completedslpckg_message;
    }

    public void setCompletedslpckg_message(CompleteDSLPckg_Message completedslpckg_message) {
        this.completedslpckg_message = completedslpckg_message;
    }
    public CompleteDSLPckg_Connector getCompletedslpckg_connector() {
        return completedslpckg_connector;
    }

    public void setCompletedslpckg_connector(CompleteDSLPckg_Connector completedslpckg_connector) {
        this.completedslpckg_connector = completedslpckg_connector;
    }
    public List<CompleteDSLPckg_Behavior> getCompletedslpckg_behaviors() {
        return completedslpckg_behaviors;
    }

    public void addCompletedslpckg_behavior(Completedslpckg_behavior completedslpckg_behavior) {
        this.completedslpckg_behaviors.add(completedslpckg_behavior);
    }

}