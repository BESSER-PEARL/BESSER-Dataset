





import java.util.List;
import java.util.ArrayList;

public class umlclassdiagram_Attribute extends Feature {

    private boolean derived;



    public umlclassdiagram_Attribute(
        boolean derived    ) {
        super(
        );
        this.derived = derived;
    }


    public boolean getDerived() {
        return derived;
    }

    public void setDerived(boolean derived) {
        this.derived = derived;
    }


}