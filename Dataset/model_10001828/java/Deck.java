





import java.util.List;
import java.util.ArrayList;

public class Deck  {

    private String attribute;





    private Elevens elevens;


    public Deck(
        String attribute    ) {
        this.attribute = attribute;
    }


    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }

    public Elevens getElevens() {
        return elevens;
    }

    public void setElevens(Elevens elevens) {
        this.elevens = elevens;
    }

}