





import java.util.List;
import java.util.ArrayList;

public class facademapping_FacadeMappping  {






    private List<facademapping_Mapping> facademapping_mappings;


    public facademapping_FacadeMappping(
    ) {
        this.facademapping_mappings = new ArrayList<>();
    }

    public facademapping_FacadeMappping(
        ArrayList<facademapping_Mapping> facademapping_mappings    ) {
        this.facademapping_mappings = facademapping_mappings;
    }


    public List<facademapping_Mapping> getFacademapping_mappings() {
        return facademapping_mappings;
    }

    public void addFacademapping_mapping(Facademapping_mapping facademapping_mapping) {
        this.facademapping_mappings.add(facademapping_mapping);
    }

}