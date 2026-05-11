





import java.util.List;
import java.util.ArrayList;

public class swt_Separator extends Control {

    private String orientationStyle;



    public swt_Separator(
        String orientationStyle    ) {
        super(
        );
        this.orientationStyle = orientationStyle;
    }


    public String getOrientationstyle() {
        return orientationStyle;
    }

    public void setOrientationstyle(String orientationStyle) {
        this.orientationStyle = orientationStyle;
    }


}