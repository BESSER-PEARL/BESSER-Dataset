





import java.util.List;
import java.util.ArrayList;

public class UML2_Operation extends MultiplicityElement, BehavioralFeature, TypedElement, ParameterableElement {

    private boolean isQuery;



    public UML2_Operation(
        boolean isQuery    ) {
        super(
        );
        this.isQuery = isQuery;
    }


    public boolean getIsquery() {
        return isQuery;
    }

    public void setIsquery(boolean isQuery) {
        this.isQuery = isQuery;
    }


}