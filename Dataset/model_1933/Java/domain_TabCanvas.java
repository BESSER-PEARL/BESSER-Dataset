





import java.util.List;
import java.util.ArrayList;

public class domain_TabCanvas extends Categorized, DefaultCavas, CanvasFrame, MultiLangLabel {

    private String orientation;



    public domain_TabCanvas(
        String orientation    ) {
        super(
        );
        this.orientation = orientation;
    }


    public String getOrientation() {
        return orientation;
    }

    public void setOrientation(String orientation) {
        this.orientation = orientation;
    }


}