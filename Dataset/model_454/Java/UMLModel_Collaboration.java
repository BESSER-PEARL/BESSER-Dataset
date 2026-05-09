





import java.util.List;
import java.util.ArrayList;

public class UMLModel_Collaboration extends StructuredClassifier, BehavioredClassifier {

    private String collaborationRole;



    public UMLModel_Collaboration(
        String collaborationRole    ) {
        super(
        );
        this.collaborationRole = collaborationRole;
    }


    public String getCollaborationrole() {
        return collaborationRole;
    }

    public void setCollaborationrole(String collaborationRole) {
        this.collaborationRole = collaborationRole;
    }


}