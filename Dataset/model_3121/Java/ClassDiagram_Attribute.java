





import java.util.List;
import java.util.ArrayList;

public class ClassDiagram_Attribute extends NamedElement {

    private String multiValued;



    public ClassDiagram_Attribute(
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