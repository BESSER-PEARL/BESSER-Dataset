





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_EdgeMappingImport extends description_DocumentedElement, description_IEdgeMapping, description_IdentifiedElement {

    private boolean inheritsAncestorFilters;



    public viewpoint_description_EdgeMappingImport(
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