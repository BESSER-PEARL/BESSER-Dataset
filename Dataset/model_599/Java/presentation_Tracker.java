





import java.util.List;
import java.util.ArrayList;

public class presentation_Tracker extends Widget {

    private String stippled;
    private String rectangles;
    private String group;



    public presentation_Tracker(
        String stippled,        String rectangles,        String group    ) {
        super(
        );
        this.stippled = stippled;
        this.rectangles = rectangles;
        this.group = group;
    }


    public String getStippled() {
        return stippled;
    }

    public void setStippled(String stippled) {
        this.stippled = stippled;
    }
    public String getRectangles() {
        return rectangles;
    }

    public void setRectangles(String rectangles) {
        this.rectangles = rectangles;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }


}