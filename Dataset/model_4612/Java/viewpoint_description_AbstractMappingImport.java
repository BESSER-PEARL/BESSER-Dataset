





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_AbstractMappingImport  {

    private boolean hideSubMappings;
    private boolean inheritsAncestorFilters;



    public viewpoint_description_AbstractMappingImport(
        boolean hideSubMappings,        boolean inheritsAncestorFilters    ) {
        this.hideSubMappings = hideSubMappings;
        this.inheritsAncestorFilters = inheritsAncestorFilters;
    }


    public boolean getHidesubmappings() {
        return hideSubMappings;
    }

    public void setHidesubmappings(boolean hideSubMappings) {
        this.hideSubMappings = hideSubMappings;
    }
    public boolean getInheritsancestorfilters() {
        return inheritsAncestorFilters;
    }

    public void setInheritsancestorfilters(boolean inheritsAncestorFilters) {
        this.inheritsAncestorFilters = inheritsAncestorFilters;
    }


}