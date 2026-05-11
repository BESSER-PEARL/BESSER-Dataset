





import java.util.List;
import java.util.ArrayList;

public class effbd106_SequenceNode  {

    private String name;
    private int tMin;
    private int tMax;





    private List<effbd106_SequenceNode> effbd106_sequencenodes;


    public effbd106_SequenceNode(
        String name,        int tMin,        int tMax    ) {
        this.name = name;
        this.tMin = tMin;
        this.tMax = tMax;
        this.effbd106_sequencenodes = new ArrayList<>();
    }

    public effbd106_SequenceNode(
        String name,        int tMin,        int tMax        ArrayList<effbd106_SequenceNode> effbd106_sequencenodes    ) {
        this.name = name;
        this.tMin = tMin;
        this.tMax = tMax;
        this.effbd106_sequencenodes = effbd106_sequencenodes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getTmin() {
        return tMin;
    }

    public void setTmin(int tMin) {
        this.tMin = tMin;
    }
    public int getTmax() {
        return tMax;
    }

    public void setTmax(int tMax) {
        this.tMax = tMax;
    }

    public List<effbd106_SequenceNode> getEffbd106_sequencenodes() {
        return effbd106_sequencenodes;
    }

    public void addEffbd106_sequencenode(Effbd106_sequencenode effbd106_sequencenode) {
        this.effbd106_sequencenodes.add(effbd106_sequencenode);
    }

}