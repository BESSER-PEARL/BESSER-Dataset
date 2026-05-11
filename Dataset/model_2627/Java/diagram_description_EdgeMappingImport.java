





import java.util.List;
import java.util.ArrayList;

public class diagram_description_EdgeMappingImport extends description_IdentifiedElement, description_DocumentedElement, description_IEdgeMapping {

    private boolean inheritsAncestorFilters;



    public diagram_description_EdgeMappingImport(
        boolean inheritsAncestorFilters    ) {
        super(
        );
        this.inheritsAncestorFilters = inheritsAncestorFilters;
    }


    public boolean getInheritsancestorfilters() {
        return inheritsAncestorFilters;
    }

    public void setInheritsancestorfilters(boolean inheritsAncestorFilters) {
        this.inheritsAncestorFilters = inheritsAncestorFilters;
    }


}