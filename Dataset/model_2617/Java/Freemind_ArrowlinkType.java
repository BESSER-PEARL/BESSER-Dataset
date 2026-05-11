





import java.util.List;
import java.util.ArrayList;

public class Freemind_ArrowlinkType  {

    private String StartArrow;
    private String EndArrow;
    private String StartInclination;
    private String EndInclination;
    private String Id;
    private String Destination;
    private String Color;



    public Freemind_ArrowlinkType(
        String StartArrow,        String EndArrow,        String StartInclination,        String EndInclination,        String Id,        String Destination,        String Color    ) {
        this.StartArrow = StartArrow;
        this.EndArrow = EndArrow;
        this.StartInclination = StartInclination;
        this.EndInclination = EndInclination;
        this.Id = Id;
        this.Destination = Destination;
        this.Color = Color;
    }


    public String getStartarrow() {
        return StartArrow;
    }

    public void setStartarrow(String StartArrow) {
        this.StartArrow = StartArrow;
    }
    public String getEndarrow() {
        return EndArrow;
    }

    public void setEndarrow(String EndArrow) {
        this.EndArrow = EndArrow;
    }
    public String getStartinclination() {
        return StartInclination;
    }

    public void setStartinclination(String StartInclination) {
        this.StartInclination = StartInclination;
    }
    public String getEndinclination() {
        return EndInclination;
    }

    public void setEndinclination(String EndInclination) {
        this.EndInclination = EndInclination;
    }
    public String getId() {
        return Id;
    }

    public void setId(String Id) {
        this.Id = Id;
    }
    public String getDestination() {
        return Destination;
    }

    public void setDestination(String Destination) {
        this.Destination = Destination;
    }
    public String getColor() {
        return Color;
    }

    public void setColor(String Color) {
        this.Color = Color;
    }


}