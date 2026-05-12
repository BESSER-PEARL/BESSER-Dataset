





import java.util.List;
import java.util.ArrayList;

public class extendedpetrinet_InputPlaceAppearance extends Label {

    private String text;





    private extendedpetrinet_Place extendedpetrinet_place;


    public extendedpetrinet_InputPlaceAppearance(
        String text    ) {
        super(
        );
        this.text = text;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public extendedpetrinet_Place getExtendedpetrinet_place() {
        return extendedpetrinet_place;
    }

    public void setExtendedpetrinet_place(extendedpetrinet_Place extendedpetrinet_place) {
        this.extendedpetrinet_place = extendedpetrinet_place;
    }

}