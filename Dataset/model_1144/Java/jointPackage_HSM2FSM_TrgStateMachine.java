





import java.util.List;
import java.util.ArrayList;

public class jointPackage_HSM2FSM_TrgStateMachine  {

    private String name;





    private List<TrgAbstractState> trgabstractstates;


    public jointPackage_HSM2FSM_TrgStateMachine(
        String name    ) {
        this.name = name;
        this.trgabstractstates = new ArrayList<>();
    }

    public jointPackage_HSM2FSM_TrgStateMachine(
        String name        ArrayList<TrgAbstractState> trgabstractstates    ) {
        this.name = name;
        this.trgabstractstates = trgabstractstates;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<TrgAbstractState> getTrgabstractstates() {
        return trgabstractstates;
    }

    public void addTrgabstractstate(Trgabstractstate trgabstractstate) {
        this.trgabstractstates.add(trgabstractstate);
    }

}