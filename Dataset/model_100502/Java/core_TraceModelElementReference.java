





import java.util.List;
import java.util.ArrayList;

public class core_TraceModelElementReference extends ModelElementReference, RequirementsCoverageData {

    private boolean container;



    public core_TraceModelElementReference(
        boolean container    ) {
        super(
        );
        this.container = container;
    }


    public boolean getContainer() {
        return container;
    }

    public void setContainer(boolean container) {
        this.container = container;
    }


}