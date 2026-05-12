





import java.util.List;
import java.util.ArrayList;

public class petrinet_InputPlace extends Attribute {

    private boolean text;





    private petrinet_Place petrinet_place;


    public petrinet_InputPlace(
        boolean text    ) {
        super(
        );
        this.text = text;
    }


    public boolean getText() {
        return text;
    }

    public void setText(boolean text) {
        this.text = text;
    }

    public petrinet_Place getPetrinet_place() {
        return petrinet_place;
    }

    public void setPetrinet_place(petrinet_Place petrinet_place) {
        this.petrinet_place = petrinet_place;
    }

}