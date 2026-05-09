





import java.util.List;
import java.util.ArrayList;

public class gfsm_IntBlock extends IntOperation {






    private List<gfsm_IntVarAssign> gfsm_intvarassigns;


    public gfsm_IntBlock(
    ) {
        super(
        );
        this.gfsm_intvarassigns = new ArrayList<>();
    }

    public gfsm_IntBlock(
        ArrayList<gfsm_IntVarAssign> gfsm_intvarassigns    ) {
        this.gfsm_intvarassigns = gfsm_intvarassigns;
    }


    public List<gfsm_IntVarAssign> getGfsm_intvarassigns() {
        return gfsm_intvarassigns;
    }

    public void addGfsm_intvarassign(Gfsm_intvarassign gfsm_intvarassign) {
        this.gfsm_intvarassigns.add(gfsm_intvarassign);
    }

}