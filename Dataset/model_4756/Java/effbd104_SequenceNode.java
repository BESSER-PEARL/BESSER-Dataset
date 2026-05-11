





import java.util.List;
import java.util.ArrayList;

public class effbd104_SequenceNode  {

    private int tMax;
    private String name;
    private int tMin;





    private effbd104_SequenceNode effbd104_sequencenode;


    public effbd104_SequenceNode(
        int tMax,        String name,        int tMin    ) {
        this.tMax = tMax;
        this.name = name;
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
    public int getTmin() {
        return tMin;
    }

    public void setTmin(int tMin) {
        this.tMin = tMin;
    }

    public effbd104_SequenceNode getEffbd104_sequencenode() {
        return effbd104_sequencenode;
    }

    public void setEffbd104_sequencenode(effbd104_SequenceNode effbd104_sequencenode) {
        this.effbd104_sequencenode = effbd104_sequencenode;
    }

}