





import java.util.List;
import java.util.ArrayList;

public class fsm_RuntimeConcept2  {

    private String bar;





    private List<fsm_RuntimeConcept1> fsm_runtimeconcept1s;


    public fsm_RuntimeConcept2(
        String bar    ) {
        this.bar = bar;
        this.fsm_runtimeconcept1s = new ArrayList<>();
    }

    public fsm_RuntimeConcept2(
        String bar        ArrayList<fsm_RuntimeConcept1> fsm_runtimeconcept1s    ) {
        this.bar = bar;
        this.fsm_runtimeconcept1s = fsm_runtimeconcept1s;
    }

    public String getBar() {
        return bar;
    }

    public void setBar(String bar) {
        this.bar = bar;
    }

    public List<fsm_RuntimeConcept1> getFsm_runtimeconcept1s() {
        return fsm_runtimeconcept1s;
    }

    public void addFsm_runtimeconcept1(Fsm_runtimeconcept1 fsm_runtimeconcept1) {
        this.fsm_runtimeconcept1s.add(fsm_runtimeconcept1);
    }

}