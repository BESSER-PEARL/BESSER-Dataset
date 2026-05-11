





import java.util.List;
import java.util.ArrayList;

public class scxml_AbstractState  {






    private List<scxml_SimpleState> scxml_simplestates;


    public scxml_AbstractState(
    ) {
        this.scxml_simplestates = new ArrayList<>();
    }

    public scxml_AbstractState(
        ArrayList<scxml_SimpleState> scxml_simplestates    ) {
        this.scxml_simplestates = scxml_simplestates;
    }


    public List<scxml_SimpleState> getScxml_simplestates() {
        return scxml_simplestates;
    }

    public void addScxml_simplestate(Scxml_simplestate scxml_simplestate) {
        this.scxml_simplestates.add(scxml_simplestate);
    }

}