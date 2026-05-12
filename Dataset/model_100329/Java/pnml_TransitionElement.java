





import java.util.List;
import java.util.ArrayList;

public class pnml_TransitionElement extends Element {

    private String name;





    private pnml_ArcPlace2Transition pnml_arcplace2transition;


    public pnml_TransitionElement(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public pnml_ArcPlace2Transition getPnml_arcplace2transition() {
        return pnml_arcplace2transition;
    }

    public void setPnml_arcplace2transition(pnml_ArcPlace2Transition pnml_arcplace2transition) {
        this.pnml_arcplace2transition = pnml_arcplace2transition;
    }

}