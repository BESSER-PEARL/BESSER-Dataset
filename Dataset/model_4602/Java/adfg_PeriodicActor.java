





import java.util.List;
import java.util.ArrayList;

public class adfg_PeriodicActor extends Actor {

    private String periodLowerBound;
    private String period;
    private String wcet;
    private String periodUpperBound;
    private String phase;
    private String deadline;





    private List<adfg_AffineRelation> adfg_affinerelations;




    private adfg_AffineRelation adfg_affinerelation;




    private List<adfg_AffineRelation> adfg_affinerelations;




    private adfg_AffineRelation adfg_affinerelation;


    public adfg_PeriodicActor(
        String periodLowerBound,        String period,        String wcet,        String periodUpperBound,        String phase,        String deadline    ) {
        super(
        );
        this.periodLowerBound = periodLowerBound;
        this.period = period;
        this.wcet = wcet;
        this.periodUpperBound = periodUpperBound;
        this.phase = phase;
        this.deadline = deadline;
        this.adfg_affinerelations = new ArrayList<>();
        this.adfg_affinerelations = new ArrayList<>();
    }

    public adfg_PeriodicActor(
        String periodLowerBound,        String period,        String wcet,        String periodUpperBound,        String phase,        String deadline        ArrayList<adfg_AffineRelation> adfg_affinerelations,        ArrayList<adfg_AffineRelation> adfg_affinerelations    ) {
        this.periodLowerBound = periodLowerBound;
        this.period = period;
        this.wcet = wcet;
        this.periodUpperBound = periodUpperBound;
        this.phase = phase;
        this.deadline = deadline;
        this.adfg_affinerelations = adfg_affinerelations;
        this.adfg_affinerelations = adfg_affinerelations;
    }

    public String getPeriodlowerbound() {
        return periodLowerBound;
    }

    public void setPeriodlowerbound(String periodLowerBound) {
        this.periodLowerBound = periodLowerBound;
    }
    public String getPeriod() {
        return period;
    }

    public void setPeriod(String period) {
        this.period = period;
    }
    public String getWcet() {
        return wcet;
    }

    public void setWcet(String wcet) {
        this.wcet = wcet;
    }
    public String getPeriodupperbound() {
        return periodUpperBound;
    }

    public void setPeriodupperbound(String periodUpperBound) {
        this.periodUpperBound = periodUpperBound;
    }
    public String getPhase() {
        return phase;
    }

    public void setPhase(String phase) {
        this.phase = phase;
    }
    public String getDeadline() {
        return deadline;
    }

    public void setDeadline(String deadline) {
        this.deadline = deadline;
    }

    public List<adfg_AffineRelation> getAdfg_affinerelations() {
        return adfg_affinerelations;
    }

    public void addAdfg_affinerelation(Adfg_affinerelation adfg_affinerelation) {
        this.adfg_affinerelations.add(adfg_affinerelation);
    }
    public adfg_AffineRelation getAdfg_affinerelation() {
        return adfg_affinerelation;
    }

    public void setAdfg_affinerelation(adfg_AffineRelation adfg_affinerelation) {
        this.adfg_affinerelation = adfg_affinerelation;
    }
    public List<adfg_AffineRelation> getAdfg_affinerelations() {
        return adfg_affinerelations;
    }

    public void addAdfg_affinerelation(Adfg_affinerelation adfg_affinerelation) {
        this.adfg_affinerelations.add(adfg_affinerelation);
    }
    public adfg_AffineRelation getAdfg_affinerelation() {
        return adfg_affinerelation;
    }

    public void setAdfg_affinerelation(adfg_AffineRelation adfg_affinerelation) {
        this.adfg_affinerelation = adfg_affinerelation;
    }

}