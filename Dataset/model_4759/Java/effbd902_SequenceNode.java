





import java.util.List;
import java.util.ArrayList;

public class effbd902_SequenceNode  {

    private String name;
    private int tMin;
    private int tMax;





    private List<effbd902_SequenceNode> effbd902_sequencenodes;


    public effbd902_SequenceNode(
        String name,        int tMin,        int tMax    ) {
        this.name = name;
        this.tMin = tMin;
        this.tMax = tMax;
        this.effbd902_sequencenodes = new ArrayList<>();
    }

    public effbd902_SequenceNode(
        String name,        int tMin,        int tMax        ArrayList<effbd902_SequenceNode> effbd902_sequencenodes    ) {
        this.name = name;
        this.tMin = tMin;
        this.tMax = tMax;
        this.effbd902_sequencenodes = effbd902_sequencenodes;
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

    public List<effbd902_SequenceNode> getEffbd902_sequencenodes() {
        return effbd902_sequencenodes;
    }

    public void addEffbd902_sequencenode(Effbd902_sequencenode effbd902_sequencenode) {
        this.effbd902_sequencenodes.add(effbd902_sequencenode);
    }

}