





import java.util.List;
import java.util.ArrayList;

public class diagram_description_DiagramElementMapping extends description_PasteTargetDescription, description_RepresentationElementMapping {

    private boolean createElements;
    private String semanticCandidatesExpression;
    private String preconditionExpression;
    private String semanticElements;
    private boolean synchronizationLock;



    public diagram_description_DiagramElementMapping(
        boolean createElements,        String semanticCandidatesExpression,        String preconditionExpression,        String semanticElements,        boolean synchronizationLock    ) {
        super(
        );
        this.createElements = createElements;
        this.semanticCandidatesExpression = semanticCandidatesExpression;
        this.preconditionExpression = preconditionExpression;
        this.semanticElements = semanticElements;
        this.synchronizationLock = synchronizationLock;
    }


    public boolean getCreateelements() {
        return createElements;
    }

    public void setCreateelements(boolean createElements) {
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
    public String getSemanticelements() {
        return semanticElements;
    }

    public void setSemanticelements(String semanticElements) {
        this.semanticElements = semanticElements;
    }
    public boolean getSynchronizationlock() {
        return synchronizationLock;
    }

    public void setSynchronizationlock(boolean synchronizationLock) {
        this.synchronizationLock = synchronizationLock;
    }


}