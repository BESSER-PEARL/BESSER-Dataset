





import java.util.List;
import java.util.ArrayList;

public class model_DiagramModelArchimateConnection extends DiagramModelConnection, DiagramModelArchimateComponent {






    private model_ArchimateRelationship model_archimaterelationship;


    public model_DiagramModelArchimateConnection(
    ) {
        super(
        );
    }



    public model_ArchimateRelationship getModel_archimaterelationship() {
        return model_archimaterelationship;
    }

    public void setModel_archimaterelationship(model_ArchimateRelationship model_archimaterelationship) {
        this.model_archimaterelationship = model_archimaterelationship;
    }

}