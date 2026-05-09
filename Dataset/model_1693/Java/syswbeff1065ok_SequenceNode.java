





import java.util.List;
import java.util.ArrayList;

public class syswbeff1065ok_SequenceNode  {

    private String name;
    private int tMin;
    private int tMax;





    private syswbeff1065ok_SequenceNode syswbeff1065ok_sequencenode;


    public syswbeff1065ok_SequenceNode(
        String name,        int tMin,        int tMax    ) {
        this.name = name;
        this.tMin = tMin;
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
    public int getTmax() {
        return tMax;
    }

    public void setTmax(int tMax) {
        this.tMax = tMax;
    }

    public syswbeff1065ok_SequenceNode getSyswbeff1065ok_sequencenode() {
        return syswbeff1065ok_sequencenode;
    }

    public void setSyswbeff1065ok_sequencenode(syswbeff1065ok_SequenceNode syswbeff1065ok_sequencenode) {
        this.syswbeff1065ok_sequencenode = syswbeff1065ok_sequencenode;
    }

}