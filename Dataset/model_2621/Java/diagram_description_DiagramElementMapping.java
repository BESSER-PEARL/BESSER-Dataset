





import java.util.List;
import java.util.ArrayList;

public class diagram_description_DiagramElementMapping extends description_RepresentationElementMapping, description_PasteTargetDescription {

    private String semanticCandidatesExpression;
    private String preconditionExpression;
    private boolean synchronizationLock;
    private String semanticElements;
    private boolean createElements;



    public diagram_description_DiagramElementMapping(
        String semanticCandidatesExpression,        String preconditionExpression,        boolean synchronizationLock,        String semanticElements,        boolean createElements    ) {
        super(
        );
        this.semanticCandidatesExpression = semanticCandidatesExpression;
        this.preconditionExpression = preconditionExpression;
        this.synchronizationLock = synchronizationLock;
        this.semanticElements = semanticElements;
        this.createElements = createElements;
    }


    public String getSemanticcandidatesexpression() {
        return semanticCandidatesExpression;
    }

    public void setSemanticcandidatesexpression(String semanticCandidatesExpression) {
        this.semanticCandidatesExpression = semanticCandidatesExpression;
    }
    public String getPreconditionexpression() {
        return preconditionExpression;
    }

    public void setPreconditionexpression(String preconditionExpression) {
        this.preconditionExpression = preconditionExpression;
    }
    public boolean getSynchronizationlock() {
        return synchronizationLock;
    }

    public void setSynchronizationlock(boolean synchronizationLock) {
        this.synchronizationLock = synchronizationLock;
    }
    public String getSemanticelements() {
        return semanticElements;
    }

    public void setSemanticelements(String semanticElements) {
        this.semanticElements = semanticElements;
    }
    public boolean getCreateelements() {
        return createElements;
    }

    public void setCreateelements(boolean createElements) {
        this.createElements = createElements;
    }


}