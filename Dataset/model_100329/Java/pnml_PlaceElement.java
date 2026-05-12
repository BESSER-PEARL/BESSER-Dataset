





import java.util.List;
import java.util.ArrayList;

public class pnml_PlaceElement extends Element {

    private int tokens;
    private String name;





    private pnml_ArcPlace2Transition pnml_arcplace2transition;


    public pnml_PlaceElement(
        int tokens,        String name    ) {
        super(
        );
        this.tokens = tokens;
        this.name = name;
    }


    public int getTokens() {
        return tokens;
    }

    public void setTokens(int tokens) {
        this.tokens = tokens;
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