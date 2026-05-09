





import java.util.List;
import java.util.ArrayList;

public class xmof_IntermediateActions_LinkAction extends Action {






    private List<BasicActions_InputPin> basicactions_inputpins;


    public xmof_IntermediateActions_LinkAction(
    ) {
        super(
        );
        this.basicactions_inputpins = new ArrayList<>();
    }

    public xmof_IntermediateActions_LinkAction(
        ArrayList<BasicActions_InputPin> basicactions_inputpins    ) {
        this.basicactions_inputpins = basicactions_inputpins;
    }


    public List<BasicActions_InputPin> getBasicactions_inputpins() {
        return basicactions_inputpins;
    }

    public void addBasicactions_inputpin(Basicactions_inputpin basicactions_inputpin) {
        this.basicactions_inputpins.add(basicactions_inputpin);
    }

}