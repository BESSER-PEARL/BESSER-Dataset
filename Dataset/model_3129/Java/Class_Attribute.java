





import java.util.List;
import java.util.ArrayList;

public class Class_Attribute extends NamedElt {

    private boolean multiValued;





    private Class class;


    public Class_Attribute(
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

    public Class getClass() {
        return class;
    }

    public void setClass(Class class) {
        this.class = class;
    }

}