





import java.util.List;
import java.util.ArrayList;

public class Class_Attribute extends NamedElt {

    private String multiValued;



    public Class_Attribute(
        String multiValued    ) {
        super(
        );
        this.multiValued = multiValued;
    }


    public String getMultivalued() {
        return multiValued;
    }

    public void setMultivalued(String multiValued) {
        this.multiValued = multiValued;
    }


}