





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLSimplified_Row extends ColOrRowElement {

    private float height;
    private boolean autoFitHeight;



    public SpreadsheetMLSimplified_Row(
        float height,        boolean autoFitHeight    ) {
        super(
        );
        this.height = height;
        this.autoFitHeight = autoFitHeight;
    }


    public float getHeight() {
        return height;
    }

    public void setHeight(float height) {
        this.height = height;
    }
    public boolean getAutofitheight() {
        return autoFitHeight;
    }

    public void setAutofitheight(boolean autoFitHeight) {
        this.autoFitHeight = autoFitHeight;
    }


}