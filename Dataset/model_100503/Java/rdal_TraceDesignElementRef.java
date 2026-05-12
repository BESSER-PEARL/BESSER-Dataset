





import java.util.List;
import java.util.ArrayList;

public class rdal_TraceDesignElementRef extends RequirementsCoverageData, VerifiableElement, DesignElementReference {

    private boolean container;



    public rdal_TraceDesignElementRef(
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