





import java.util.List;
import java.util.ArrayList;

public class diagram_description_DiagramElementMapping extends description_RepresentationElementMapping, description_PasteTargetDescription {

    private String preconditionExpression;
    private String semanticCandidatesExpression;
    private boolean createElements;
    private String semanticElements;
    private boolean synchronizationLock;



    public diagram_description_DiagramElementMapping(
        String preconditionExpression,        String semanticCandidatesExpression,        boolean createElements,        String semanticElements,        boolean synchronizationLock    ) {
        super(
        );
        this.preconditionExpression = preconditionExpression;
        this.semanticCandidatesExpression = semanticCandidatesExpression;
        this.createElements = createElements;
        this.semanticElements = semanticElements;
        this.synchronizationLock = synchronizationLock;
    }


    public String getPreconditionexpression() {
        return preconditionExpression;
    }

    public void setPreconditionexpression(String preconditionExpression) {
        this.preconditionExpression = preconditionExpression;
    }
    public String getSemanticcandidatesexpression() {
        return semanticCandidatesExpression;
    }

    public void setSemanticcandidatesexpression(String semanticCandidatesExpression) {
        this.semanticCandidatesExpression = semanticCandidatesExpression;
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
    public boolean getSynchronizationlock() {
        return synchronizationLock;
    }

    public void setSynchronizationlock(boolean synchronizationLock) {
        this.synchronizationLock = synchronizationLock;
    }


}