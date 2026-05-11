





import java.util.List;
import java.util.ArrayList;

public class effbd201_SequenceNode  {

    private int tMin;
    private int tMax;
    private String name;





    private effbd201_SequenceNode effbd201_sequencenode;


    public effbd201_SequenceNode(
        int tMin,        int tMax,        String name    ) {
        this.tMin = tMin;
        this.tMax = tMax;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public effbd201_SequenceNode getEffbd201_sequencenode() {
        return effbd201_sequencenode;
    }

    public void setEffbd201_sequencenode(effbd201_SequenceNode effbd201_sequencenode) {
        this.effbd201_sequencenode = effbd201_sequencenode;
    }

}