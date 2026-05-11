





import java.util.List;
import java.util.ArrayList;

public class diagram_description_DiagramElementMapping extends description_RepresentationElementMapping, description_PasteTargetDescription {

    private boolean createElements;
    private String semanticElements;
    private String semanticCandidatesExpression;
    private boolean synchronizationLock;
    private String preconditionExpression;



    public diagram_description_DiagramElementMapping(
        boolean createElements,        String semanticElements,        String semanticCandidatesExpression,        boolean synchronizationLock,        String preconditionExpression    ) {
        super(
        );
        this.createElements = createElements;
        this.semanticElements = semanticElements;
        this.semanticCandidatesExpression = semanticCandidatesExpression;
        this.synchronizationLock = synchronizationLock;
        this.preconditionExpression = preconditionExpression;
    }


    public boolean getCreateelements() {
        return createElements;
    }

    public void setCreateelements(boolean createElements) {
        this.createElements = createElements;
    }
    public String getSemanticelements() {
        return semanticElements;
    }

    public void setSemanticelements(String semanticElements) {
        this.semanticElements = semanticElements;
    }
    public String getSemanticcandidatesexpression() {
        return semanticCandidatesExpression;
    }

    public void setSemanticcandidatesexpression(String semanticCandidatesExpression) {
        this.semanticCandidatesExpression = semanticCandidatesExpression;
    }
    public boolean getSynchronizationlock() {
        return synchronizationLock;
    }

    public void setSynchronizationlock(boolean synchronizationLock) {
        this.synchronizationLock = synchronizationLock;
    }
    public String getPreconditionexpression() {
        return preconditionExpression;
    }

    public void setPreconditionexpression(String preconditionExpression) {
        this.preconditionExpression = preconditionExpression;
    }


}