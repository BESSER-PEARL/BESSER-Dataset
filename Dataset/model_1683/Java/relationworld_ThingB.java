





import java.util.List;
import java.util.ArrayList;

public class relationworld_ThingB extends TargetNode, NamedElement {

    private String step;





    private relationworld_RelatedTo relationworld_relatedto;


    public relationworld_ThingB(
        String step    ) {
        super(
        );
        this.step = step;
    }


    public String getStep() {
        return step;
    }

    public void setStep(String step) {
        this.step = step;
    }

    public relationworld_RelatedTo getRelationworld_relatedto() {
        return relationworld_relatedto;
    }

    public void setRelationworld_relatedto(relationworld_RelatedTo relationworld_relatedto) {
        this.relationworld_relatedto = relationworld_relatedto;
    }

}