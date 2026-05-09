





import java.util.List;
import java.util.ArrayList;

public class petrinet_Place extends Node {

    private String id;
    private String markings;





    private petrinet_PNGraph petrinet_pngraph;


    public petrinet_Place(
        String id,        String markings    ) {
        super(
        );
        this.id = id;
        this.markings = markings;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getMarkings() {
        return markings;
    }

    public void setMarkings(String markings) {
        this.markings = markings;
    }

    public petrinet_PNGraph getPetrinet_pngraph() {
        return petrinet_pngraph;
    }

    public void setPetrinet_pngraph(petrinet_PNGraph petrinet_pngraph) {
        this.petrinet_pngraph = petrinet_pngraph;
    }

}