





import java.util.List;
import java.util.ArrayList;

public class carnot_IConnectionSymbol extends IGraphicalObject {

    private String sourceAnchor;
    private String targetAnchor;
    private String routing;





    private List<carnot_Coordinates> carnot_coordinatess;


    public carnot_IConnectionSymbol(
        String sourceAnchor,        String targetAnchor,        String routing    ) {
        super(
        );
        this.sourceAnchor = sourceAnchor;
        this.targetAnchor = targetAnchor;
        this.routing = routing;
        this.carnot_coordinatess = new ArrayList<>();
    }

    public carnot_IConnectionSymbol(
        String sourceAnchor,        String targetAnchor,        String routing        ArrayList<carnot_Coordinates> carnot_coordinatess    ) {
        this.sourceAnchor = sourceAnchor;
        this.targetAnchor = targetAnchor;
        this.routing = routing;
        this.carnot_coordinatess = carnot_coordinatess;
    }

    public String getSourceanchor() {
        return sourceAnchor;
    }

    public void setSourceanchor(String sourceAnchor) {
        this.sourceAnchor = sourceAnchor;
    }
    public String getTargetanchor() {
        return targetAnchor;
    }

    public void setTargetanchor(String targetAnchor) {
        this.targetAnchor = targetAnchor;
    }
    public String getRouting() {
        return routing;
    }

    public void setRouting(String routing) {
        this.routing = routing;
    }

    public List<carnot_Coordinates> getCarnot_coordinatess() {
        return carnot_coordinatess;
    }

    public void addCarnot_coordinates(Carnot_coordinates carnot_coordinates) {
        this.carnot_coordinatess.add(carnot_coordinates);
    }

}