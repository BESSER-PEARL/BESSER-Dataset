





import java.util.List;
import java.util.ArrayList;

public class UMLModel_Include extends NamedElement, DirectedRelationship {

    private String addition;
    private String includingCase;



    public UMLModel_Include(
        String addition,        String includingCase    ) {
        super(
        );
        this.addition = addition;
        this.includingCase = includingCase;
    }


    public String getAddition() {
        return addition;
    }

    public void setAddition(String addition) {
        this.addition = addition;
    }
    public String getIncludingcase() {
        return includingCase;
    }

    public void setIncludingcase(String includingCase) {
        this.includingCase = includingCase;
    }


}