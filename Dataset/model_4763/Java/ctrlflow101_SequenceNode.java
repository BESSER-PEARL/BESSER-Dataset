





import java.util.List;
import java.util.ArrayList;

public class ctrlflow101_SequenceNode  {

    private int tMax;
    private int tMin;
    private String name;





    private ctrlflow101_SequenceNode ctrlflow101_sequencenode;


    public ctrlflow101_SequenceNode(
        int tMax,        int tMin,        String name    ) {
        this.tMax = tMax;
        this.tMin = tMin;
        this.name = name;
    }


    public int getTmax() {
        return tMax;
    }

    public void setTmax(int tMax) {
        this.tMax = tMax;
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

    public ctrlflow101_SequenceNode getCtrlflow101_sequencenode() {
        return ctrlflow101_sequencenode;
    }

    public void setCtrlflow101_sequencenode(ctrlflow101_SequenceNode ctrlflow101_sequencenode) {
        this.ctrlflow101_sequencenode = ctrlflow101_sequencenode;
    }

}