





import java.util.List;
import java.util.ArrayList;

public class dom_Mapper extends ModelElement {

    private boolean biDirectional;
    private boolean toLeft;
    private boolean toRight;



    public dom_Mapper(
        boolean biDirectional,        boolean toLeft,        boolean toRight    ) {
        super(
        );
        this.biDirectional = biDirectional;
        this.toLeft = toLeft;
        this.toRight = toRight;
    }


    public boolean getBidirectional() {
        return biDirectional;
    }

    public void setBidirectional(boolean biDirectional) {
        this.biDirectional = biDirectional;
    }
    public boolean getToleft() {
        return toLeft;
    }

    public void setToleft(boolean toLeft) {
        this.toLeft = toLeft;
    }
    public boolean getToright() {
        return toRight;
    }

    public void setToright(boolean toRight) {
        this.toRight = toRight;
    }


}