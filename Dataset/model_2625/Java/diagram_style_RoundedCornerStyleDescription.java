





import java.util.List;
import java.util.ArrayList;

public class diagram_style_RoundedCornerStyleDescription extends StyleDescription {

    private String arcWidth;
    private String arcHeight;



    public diagram_style_RoundedCornerStyleDescription(
        String arcWidth,        String arcHeight    ) {
        super(
        );
        this.arcWidth = arcWidth;
        this.arcHeight = arcHeight;
    }


    public String getArcwidth() {
        return arcWidth;
    }

    public void setArcwidth(String arcWidth) {
        this.arcWidth = arcWidth;
    }
    public String getArcheight() {
        return arcHeight;
    }

    public void setArcheight(String arcHeight) {
        this.arcHeight = arcHeight;
    }


}