





import java.util.List;
import java.util.ArrayList;

public class diagram_description_DiagramElementMapping extends description_PasteTargetDescription, description_RepresentationElementMapping {

    private String semanticCandidatesExpression;
    private String preconditionExpression;
    private String semanticElements;
    private boolean createElements;
    private boolean synchronizationLock;



    public diagram_description_DiagramElementMapping(
        String semanticCandidatesExpression,        String preconditionExpression,        String semanticElements,        boolean createElements,        boolean synchronizationLock    ) {
        super(
        );
        this.semanticCandidatesExpression = semanticCandidatesExpression;
        this.preconditionExpression = preconditionExpression;
        this.semanticElements = semanticElements;
        this.createElements = createElements;
        this.synchronizationLock = synchronizationLock;
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
    public boolean getCreateelements() {
        return createElements;
    }

    public void setCreateelements(boolean createElements) {
        this.createElements = createElements;
    }
    public boolean getSynchronizationlock() {
        return synchronizationLock;
    }

    public void setSynchronizationlock(boolean synchronizationLock) {
        this.synchronizationLock = synchronizationLock;
    }


}