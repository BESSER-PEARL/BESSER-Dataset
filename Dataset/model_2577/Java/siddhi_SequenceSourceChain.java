





import java.util.List;
import java.util.ArrayList;

public class siddhi_SequenceSourceChain  {

    private String op;





    private siddhi_SequenceSourceChain siddhi_sequencesourcechain;




    private siddhi_EverySequenceSourceChain siddhi_everysequencesourcechain;




    private siddhi_EveryAbsentSequenceSourceChain siddhi_everyabsentsequencesourcechain;




    private List<siddhi_WithinTime> siddhi_withintimes;




    private siddhi_SequenceSourceChain siddhi_sequencesourcechain;




    private siddhi_RightAbsentSequenceSource siddhi_rightabsentsequencesource;




    private siddhi_LeftAbsentSequenceSource siddhi_leftabsentsequencesource;


    public siddhi_SequenceSourceChain(
        String op    ) {
        this.op = op;
        this.siddhi_withintimes = new ArrayList<>();
    }

    public siddhi_SequenceSourceChain(
        String op        ArrayList<siddhi_WithinTime> siddhi_withintimes    ) {
        this.op = op;
        this.siddhi_withintimes = siddhi_withintimes;
    }

    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public siddhi_SequenceSourceChain getSiddhi_sequencesourcechain() {
        return siddhi_sequencesourcechain;
    }

    public void setSiddhi_sequencesourcechain(siddhi_SequenceSourceChain siddhi_sequencesourcechain) {
        this.siddhi_sequencesourcechain = siddhi_sequencesourcechain;
    }
    public siddhi_EverySequenceSourceChain getSiddhi_everysequencesourcechain() {
        return siddhi_everysequencesourcechain;
    }

    public void setSiddhi_everysequencesourcechain(siddhi_EverySequenceSourceChain siddhi_everysequencesourcechain) {
        this.siddhi_everysequencesourcechain = siddhi_everysequencesourcechain;
    }
    public siddhi_EveryAbsentSequenceSourceChain getSiddhi_everyabsentsequencesourcechain() {
        return siddhi_everyabsentsequencesourcechain;
    }

    public void setSiddhi_everyabsentsequencesourcechain(siddhi_EveryAbsentSequenceSourceChain siddhi_everyabsentsequencesourcechain) {
        this.siddhi_everyabsentsequencesourcechain = siddhi_everyabsentsequencesourcechain;
    }
    public List<siddhi_WithinTime> getSiddhi_withintimes() {
        return siddhi_withintimes;
    }

    public void addSiddhi_withintime(Siddhi_withintime siddhi_withintime) {
        this.siddhi_withintimes.add(siddhi_withintime);
    }
    public siddhi_SequenceSourceChain getSiddhi_sequencesourcechain() {
        return siddhi_sequencesourcechain;
    }

    public void setSiddhi_sequencesourcechain(siddhi_SequenceSourceChain siddhi_sequencesourcechain) {
        this.siddhi_sequencesourcechain = siddhi_sequencesourcechain;
    }
    public siddhi_RightAbsentSequenceSource getSiddhi_rightabsentsequencesource() {
        return siddhi_rightabsentsequencesource;
    }

    public void setSiddhi_rightabsentsequencesource(siddhi_RightAbsentSequenceSource siddhi_rightabsentsequencesource) {
        this.siddhi_rightabsentsequencesource = siddhi_rightabsentsequencesource;
    }
    public siddhi_LeftAbsentSequenceSource getSiddhi_leftabsentsequencesource() {
        return siddhi_leftabsentsequencesource;
    }

    public void setSiddhi_leftabsentsequencesource(siddhi_LeftAbsentSequenceSource siddhi_leftabsentsequencesource) {
        this.siddhi_leftabsentsequencesource = siddhi_leftabsentsequencesource;
    }

}