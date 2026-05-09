





import java.util.List;
import java.util.ArrayList;

public class UMLModel_DirectedRelationship extends Relationship {

    private String source;
    private String target;



    public UMLModel_DirectedRelationship(
        String source,        String target    ) {
        super(
        );
        this.source = source;
        this.target = target;
    }


    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }
    public String getTarget() {
        return target;
    }

    public void setTarget(String target) {
        this.target = target;
    }


}