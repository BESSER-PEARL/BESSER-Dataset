





import java.util.List;
import java.util.ArrayList;

public class model_Tooltip extends SkinSupport, TextLinksSupport, TextAlignmentSupport, Widget, ColorBackgroundSupport, FontSupport {

    private String position;



    public model_Tooltip(
        String position    ) {
        super(
        );
        this.position = position;
    }


    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }


}