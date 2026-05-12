





import java.util.List;
import java.util.ArrayList;

public class nupn_UnitType  {

    private String places;
    private String subunits;
    private String id;





    private nupn_StructureType nupn_structuretype;


    public nupn_UnitType(
        String places,        String subunits,        String id    ) {
        this.places = places;
        this.subunits = subunits;
        this.id = id;
    }


    public String getPlaces() {
        return places;
    }

    public void setPlaces(String places) {
        this.places = places;
    }
    public String getSubunits() {
        return subunits;
    }

    public void setSubunits(String subunits) {
        this.subunits = subunits;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public nupn_StructureType getNupn_structuretype() {
        return nupn_structuretype;
    }

    public void setNupn_structuretype(nupn_StructureType nupn_structuretype) {
        this.nupn_structuretype = nupn_structuretype;
    }

}