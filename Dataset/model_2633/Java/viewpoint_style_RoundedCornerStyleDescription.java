





import java.util.List;
import java.util.ArrayList;

public class viewpoint_style_RoundedCornerStyleDescription extends StyleDescription {

    private String arcHeight;
    private String arcWidth;



    public viewpoint_style_RoundedCornerStyleDescription(
        String arcHeight,        String arcWidth    ) {
        super(
        );
        this.arcHeight = arcHeight;
        this.arcWidth = arcWidth;
    }


    public String getArcheight() {
        return arcHeight;
    }

    public void setArcheight(String arcHeight) {
        this.arcHeight = arcHeight;
    }
    public String getArcwidth() {
        return arcWidth;
    }

    public void setArcwidth(String arcWidth) {
        this.arcWidth = arcWidth;
    }


}