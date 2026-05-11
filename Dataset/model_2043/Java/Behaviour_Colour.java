





import java.util.List;
import java.util.ArrayList;

public class Behaviour_Colour extends Identifier {

    private String attribute;



    public Behaviour_Colour(
        String attribute    ) {
        super(
        );
        this.attribute = attribute;
    }


    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }


}