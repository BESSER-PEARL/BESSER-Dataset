





import java.util.List;
import java.util.ArrayList;

public class extendedpetrinet_InteractiveInput extends Attribute {

    private boolean text;



    public extendedpetrinet_InteractiveInput(
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


}