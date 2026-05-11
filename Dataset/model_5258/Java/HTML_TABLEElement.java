





import java.util.List;
import java.util.ArrayList;

public class HTML_TABLEElement extends BODYElement {

    private String background;
    private String bgcolor;



    public HTML_TABLEElement(
        String background,        String bgcolor    ) {
        super(
        );
        this.background = background;
        this.bgcolor = bgcolor;
    }


    public String getBackground() {
        return background;
    }

    public void setBackground(String background) {
        this.background = background;
    }
    public String getBgcolor() {
        return bgcolor;
    }

    public void setBgcolor(String bgcolor) {
        this.bgcolor = bgcolor;
    }


}