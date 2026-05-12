





import java.util.List;
import java.util.ArrayList;

public class Styling_Style  {

    private String appliedFonts;
    private String color;





    private Styling_Segment styling_segment;


    public Styling_Style(
        String appliedFonts,        String color    ) {
        this.appliedFonts = appliedFonts;
        this.color = color;
    }


    public String getAppliedfonts() {
        return appliedFonts;
    }

    public void setAppliedfonts(String appliedFonts) {
        this.appliedFonts = appliedFonts;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public Styling_Segment getStyling_segment() {
        return styling_segment;
    }

    public void setStyling_segment(Styling_Segment styling_segment) {
        this.styling_segment = styling_segment;
    }

}