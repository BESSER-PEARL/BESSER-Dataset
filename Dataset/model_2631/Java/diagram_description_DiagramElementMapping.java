





import java.util.List;
import java.util.ArrayList;

public class diagram_description_DiagramElementMapping extends description_PasteTargetDescription, description_RepresentationElementMapping {

    private boolean createElements;
    private String preconditionExpression;
    private boolean synchronizationLock;
    private String semanticCandidatesExpression;
    private String semanticElements;



    public diagram_description_DiagramElementMapping(
        boolean createElements,        String preconditionExpression,        boolean synchronizationLock,        String semanticCandidatesExpression,        String semanticElements    ) {
        super(
        );
        this.createElements = createElements;
        this.preconditionExpression = preconditionExpression;
        this.synchronizationLock = synchronizationLock;
        this.semanticCandidatesExpression = semanticCandidatesExpression;
        this.semanticElements = semanticElements;
    }


    public boolean getCreateelements() {
        return createElements;
    }

    public void setCreateelements(boolean createElements) {
        this.createElements = createElements;
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
    public String getSemanticcandidatesexpression() {
        return semanticCandidatesExpression;
    }

    public void setSemanticcandidatesexpression(String semanticCandidatesExpression) {
        this.semanticCandidatesExpression = semanticCandidatesExpression;
    }
    public String getSemanticelements() {
        return semanticElements;
    }

    public void setSemanticelements(String semanticElements) {
        this.semanticElements = semanticElements;
    }


}