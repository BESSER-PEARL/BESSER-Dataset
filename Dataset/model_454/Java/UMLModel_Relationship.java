





import java.util.List;
import java.util.ArrayList;

public class UMLModel_Relationship extends Element {

    private String relatedElement;



    public UMLModel_Relationship(
        String relatedElement    ) {
        super(
        );
        this.relatedElement = relatedElement;
    }


    public String getRelatedelement() {
        return relatedElement;
    }

    public void setRelatedelement(String relatedElement) {
        this.relatedElement = relatedElement;
    }


}