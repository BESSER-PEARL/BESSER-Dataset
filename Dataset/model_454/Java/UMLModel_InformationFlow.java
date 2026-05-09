





import java.util.List;
import java.util.ArrayList;

public class UMLModel_InformationFlow extends DirectedRelationship, PackageableElement {

    private String informationSource;
    private String conveyed;
    private String realization;
    private String realizingActivityEdge;
    private String informationTarget;
    private String realizingConnector;
    private String realizingMessage;



    public UMLModel_InformationFlow(
        String informationSource,        String conveyed,        String realization,        String realizingActivityEdge,        String informationTarget,        String realizingConnector,        String realizingMessage    ) {
        super(
        );
        this.informationSource = informationSource;
        this.conveyed = conveyed;
        this.realization = realization;
        this.realizingActivityEdge = realizingActivityEdge;
        this.informationTarget = informationTarget;
        this.realizingConnector = realizingConnector;
        this.realizingMessage = realizingMessage;
    }


    public String getInformationsource() {
        return informationSource;
    }

    public void setInformationsource(String informationSource) {
        this.informationSource = informationSource;
    }
    public String getConveyed() {
        return conveyed;
    }

    public void setConveyed(String conveyed) {
        this.conveyed = conveyed;
    }
    public String getRealization() {
        return realization;
    }

    public void setRealization(String realization) {
        this.realization = realization;
    }
    public String getRealizingactivityedge() {
        return realizingActivityEdge;
    }

    public void setRealizingactivityedge(String realizingActivityEdge) {
        this.realizingActivityEdge = realizingActivityEdge;
    }
    public String getInformationtarget() {
        return informationTarget;
    }

    public void setInformationtarget(String informationTarget) {
        this.informationTarget = informationTarget;
    }
    public String getRealizingconnector() {
        return realizingConnector;
    }

    public void setRealizingconnector(String realizingConnector) {
        this.realizingConnector = realizingConnector;
    }
    public String getRealizingmessage() {
        return realizingMessage;
    }

    public void setRealizingmessage(String realizingMessage) {
        this.realizingMessage = realizingMessage;
    }


}