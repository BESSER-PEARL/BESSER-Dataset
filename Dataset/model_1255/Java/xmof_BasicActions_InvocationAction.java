





import java.util.List;
import java.util.ArrayList;

public class xmof_BasicActions_InvocationAction extends Action {






    private List<BasicActions_InputPin> basicactions_inputpins;


    public xmof_BasicActions_InvocationAction(
    ) {
        super(
        );
        this.basicactions_inputpins = new ArrayList<>();
    }

    public xmof_BasicActions_InvocationAction(
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