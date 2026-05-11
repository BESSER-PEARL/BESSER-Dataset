





import java.util.List;
import java.util.ArrayList;

public class notation_Icon extends GraphicalElement {

    private String iconType;



    public notation_Icon(
        String iconType    ) {
        super(
        );
        this.iconType = iconType;
    }


    public String getIcontype() {
        return iconType;
    }

    public void setIcontype(String iconType) {
        this.iconType = iconType;
    }


}