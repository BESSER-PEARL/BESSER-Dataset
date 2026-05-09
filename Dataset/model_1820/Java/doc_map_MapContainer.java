





import java.util.List;
import java.util.ArrayList;

public class doc_map_MapContainer  {

    private String numberingStyle;





    private List<MapElement> mapelements;


    public doc_map_MapContainer(
        String numberingStyle    ) {
        this.numberingStyle = numberingStyle;
        this.mapelements = new ArrayList<>();
    }

    public doc_map_MapContainer(
        String numberingStyle        ArrayList<MapElement> mapelements    ) {
        this.numberingStyle = numberingStyle;
        this.mapelements = mapelements;
    }

    public String getNumberingstyle() {
        return numberingStyle;
    }

    public void setNumberingstyle(String numberingStyle) {
        this.numberingStyle = numberingStyle;
    }

    public List<MapElement> getMapelements() {
        return mapelements;
    }

    public void addMapelement(Mapelement mapelement) {
        this.mapelements.add(mapelement);
    }

}