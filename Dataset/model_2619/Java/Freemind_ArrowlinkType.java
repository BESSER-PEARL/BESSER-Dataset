





import java.util.List;
import java.util.ArrayList;

public class Freemind_ArrowlinkType  {

    private String Color;
    private String Id;
    private String EndInclination;
    private String EndArrow;
    private String StartArrow;
    private String Destination;
    private String StartInclination;



    public Freemind_ArrowlinkType(
        String Color,        String Id,        String EndInclination,        String EndArrow,        String StartArrow,        String Destination,        String StartInclination    ) {
        this.Color = Color;
        this.Id = Id;
        this.EndInclination = EndInclination;
        this.EndArrow = EndArrow;
        this.StartArrow = StartArrow;
        this.Destination = Destination;
        this.StartInclination = StartInclination;
    }


    public String getColor() {
        return Color;
    }

    public void setColor(String Color) {
        this.Color = Color;
    }
    public String getId() {
        return Id;
    }

    public void setId(String Id) {
        this.Id = Id;
    }
    public String getEndinclination() {
        return EndInclination;
    }

    public void setEndinclination(String EndInclination) {
        this.EndInclination = EndInclination;
    }
    public String getEndarrow() {
        return EndArrow;
    }

    public void setEndarrow(String EndArrow) {
        this.EndArrow = EndArrow;
    }
    public String getStartarrow() {
        return StartArrow;
    }

    public void setStartarrow(String StartArrow) {
        this.StartArrow = StartArrow;
    }
    public String getDestination() {
        return Destination;
    }

    public void setDestination(String Destination) {
        this.Destination = Destination;
    }
    public String getStartinclination() {
        return StartInclination;
    }

    public void setStartinclination(String StartInclination) {
        this.StartInclination = StartInclination;
    }


}