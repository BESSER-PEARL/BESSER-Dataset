





import java.util.List;
import java.util.ArrayList;

public class relationpattern_RelatedTo extends NamedElement, Arrow {






    private relationpattern_ThingA relationpattern_thinga;




    private relationpattern_ThingB relationpattern_thingb;


    public relationpattern_RelatedTo(
    ) {
        super(
        );
    }



    public relationpattern_ThingA getRelationpattern_thinga() {
        return relationpattern_thinga;
    }

    public void setRelationpattern_thinga(relationpattern_ThingA relationpattern_thinga) {
        this.relationpattern_thinga = relationpattern_thinga;
    }
    public relationpattern_ThingB getRelationpattern_thingb() {
        return relationpattern_thingb;
    }

    public void setRelationpattern_thingb(relationpattern_ThingB relationpattern_thingb) {
        this.relationpattern_thingb = relationpattern_thingb;
    }

}