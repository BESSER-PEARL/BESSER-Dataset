





import java.util.List;
import java.util.ArrayList;

public class draw2d_BlockFlow extends Figure {

    private String orientation;



    public draw2d_BlockFlow(
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