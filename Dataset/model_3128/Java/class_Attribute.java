





import java.util.List;
import java.util.ArrayList;

public class class_Attribute extends NamedElt {

    private boolean multiValued;



    public class_Attribute(
        boolean multiValued    ) {
        super(
        );
        this.multiValued = multiValued;
    }


    public boolean getMultivalued() {
        return multiValued;
    }

    public void setMultivalued(boolean multiValued) {
        this.multiValued = multiValued;
    }


}