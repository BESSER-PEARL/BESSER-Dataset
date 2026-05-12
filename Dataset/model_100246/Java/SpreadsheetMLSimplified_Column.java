





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLSimplified_Column extends ColOrRowElement {

    private float width;
    private boolean autoFitWidth;



    public SpreadsheetMLSimplified_Column(
        float width,        boolean autoFitWidth    ) {
        super(
        );
        this.width = width;
        this.autoFitWidth = autoFitWidth;
    }


    public float getWidth() {
        return width;
    }

    public void setWidth(float width) {
        this.width = width;
    }
    public boolean getAutofitwidth() {
        return autoFitWidth;
    }

    public void setAutofitwidth(boolean autoFitWidth) {
        this.autoFitWidth = autoFitWidth;
    }


}