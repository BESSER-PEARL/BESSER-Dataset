





import java.util.List;
import java.util.ArrayList;

public class styles_Transparent extends ColorOrGradient, ColorWithTransparency {

    private boolean transparent;



    public styles_Transparent(
        boolean transparent    ) {
        super(
        );
        this.transparent = transparent;
    }


    public boolean getTransparent() {
        return transparent;
    }

    public void setTransparent(boolean transparent) {
        this.transparent = transparent;
    }


}