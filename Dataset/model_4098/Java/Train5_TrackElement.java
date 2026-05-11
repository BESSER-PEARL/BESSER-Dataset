





import java.util.List;
import java.util.ArrayList;

public class Train5_TrackElement extends NamedElement {

    private String length;
    private String State;



    public Train5_TrackElement(
        String length,        String State    ) {
        super(
        );
        this.length = length;
        this.State = State;
    }


    public String getLength() {
        return length;
    }

    public void setLength(String length) {
        this.length = length;
    }
    public String getState() {
        return State;
    }

    public void setState(String State) {
        this.State = State;
    }


}