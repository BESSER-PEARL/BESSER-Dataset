





import java.util.List;
import java.util.ArrayList;

public class effbdpattern_SequenceNode  {

    private int tMin;
    private String name;
    private int tMax;





    private List<effbdpattern_SequenceNode> effbdpattern_sequencenodes;


    public effbdpattern_SequenceNode(
        int tMin,        String name,        int tMax    ) {
        this.tMin = tMin;
        this.name = name;
        this.tMax = tMax;
        this.effbdpattern_sequencenodes = new ArrayList<>();
    }

    public effbdpattern_SequenceNode(
        int tMin,        String name,        int tMax        ArrayList<effbdpattern_SequenceNode> effbdpattern_sequencenodes    ) {
        this.tMin = tMin;
        this.name = name;
        this.tMax = tMax;
        this.effbdpattern_sequencenodes = effbdpattern_sequencenodes;
    }

    public int getTmin() {
        return tMin;
    }

    public void setTmin(int tMin) {
        this.tMin = tMin;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getTmax() {
        return tMax;
    }

    public void setTmax(int tMax) {
        this.tMax = tMax;
    }

    public List<effbdpattern_SequenceNode> getEffbdpattern_sequencenodes() {
        return effbdpattern_sequencenodes;
    }

    public void addEffbdpattern_sequencenode(Effbdpattern_sequencenode effbdpattern_sequencenode) {
        this.effbdpattern_sequencenodes.add(effbdpattern_sequencenode);
    }

}