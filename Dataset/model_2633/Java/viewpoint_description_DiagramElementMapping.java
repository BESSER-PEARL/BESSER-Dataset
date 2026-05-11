





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_DiagramElementMapping extends description_PasteTargetDescription, description_RepresentationElementMapping {

    private String preconditionExpression;
    private String semanticCandidatesExpression;
    private String semanticElements;
    private boolean synchronizationLock;
    private boolean createElements;



    public viewpoint_description_DiagramElementMapping(
        String preconditionExpression,        String semanticCandidatesExpression,        String semanticElements,        boolean synchronizationLock,        boolean createElements    ) {
        super(
        );
        this.preconditionExpression = preconditionExpression;
        this.semanticCandidatesExpression = semanticCandidatesExpression;
        this.semanticElements = semanticElements;
        this.synchronizationLock = synchronizationLock;
        this.createElements = createElements;
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
    public boolean getCreateelements() {
        return createElements;
    }

    public void setCreateelements(boolean createElements) {
        this.createElements = createElements;
    }


}