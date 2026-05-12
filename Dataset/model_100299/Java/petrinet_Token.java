





import java.util.List;
import java.util.ArrayList;

public class petrinet_Token extends Attribute {

    private String text;





    private petrinet_Place petrinet_place;


    public petrinet_Token(
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

    public petrinet_Place getPetrinet_place() {
        return petrinet_place;
    }

    public void setPetrinet_place(petrinet_Place petrinet_place) {
        this.petrinet_place = petrinet_place;
    }

}