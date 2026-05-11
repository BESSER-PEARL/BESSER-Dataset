





import java.util.List;
import java.util.ArrayList;

public class defaultname_TABLEElement extends BODYElement {

    private String bgcolor;
    private String background;



    public defaultname_TABLEElement(
        String bgcolor,        String background    ) {
        super(
        );
        this.bgcolor = bgcolor;
        this.background = background;
    }


    public String getBgcolor() {
        return bgcolor;
    }

    public void setBgcolor(String bgcolor) {
        this.bgcolor = bgcolor;
    }
    public String getBackground() {
        return background;
    }

    public void setBackground(String background) {
        this.background = background;
    }


}