





import java.util.List;
import java.util.ArrayList;

public class MARTE_GQAM_GaStep extends GaScenario {

    private String prob;
    private String priority;
    private String servCount;
    private String blockT;
    private String rep;
    private String isAtomic;
    private String selfDelay;





    private GQAM_GaScenario gqam_gascenario;




    private GRM_SchedulableResource grm_schedulableresource;




    private List<GQAM_GaRequestedService> gqam_garequestedservices;




    private GQAM_GaScenario gqam_gascenario;


    public MARTE_GQAM_GaStep(
        String prob,        String priority,        String servCount,        String blockT,        String rep,        String isAtomic,        String selfDelay    ) {
        super(
        );
        this.prob = prob;
        this.priority = priority;
        this.servCount = servCount;
        this.blockT = blockT;
        this.rep = rep;
        this.isAtomic = isAtomic;
        this.selfDelay = selfDelay;
        this.gqam_garequestedservices = new ArrayList<>();
    }

    public MARTE_GQAM_GaStep(
        String prob,        String priority,        String servCount,        String blockT,        String rep,        String isAtomic,        String selfDelay        ArrayList<GQAM_GaRequestedService> gqam_garequestedservices    ) {
        this.prob = prob;
        this.priority = priority;
        this.servCount = servCount;
        this.blockT = blockT;
        this.rep = rep;
        this.isAtomic = isAtomic;
        this.selfDelay = selfDelay;
        this.gqam_garequestedservices = gqam_garequestedservices;
    }

    public String getProb() {
        return prob;
    }

    public void setProb(String prob) {
        this.prob = prob;
    }
    public String getPriority() {
        return priority;
    }

    public void setPriority(String priority) {
        this.priority = priority;
    }
    public String getServcount() {
        return servCount;
    }

    public void setServcount(String servCount) {
        this.servCount = servCount;
    }
    public String getBlockt() {
        return blockT;
    }

    public void setBlockt(String blockT) {
        this.blockT = blockT;
    }
    public String getRep() {
        return rep;
    }

    public void setRep(String rep) {
        this.rep = rep;
    }
    public String getIsatomic() {
        return isAtomic;
    }

    public void setIsatomic(String isAtomic) {
        this.isAtomic = isAtomic;
    }
    public String getSelfdelay() {
        return selfDelay;
    }

    public void setSelfdelay(String selfDelay) {
        this.selfDelay = selfDelay;
    }

    public GQAM_GaScenario getGqam_gascenario() {
        return gqam_gascenario;
    }

    public void setGqam_gascenario(GQAM_GaScenario gqam_gascenario) {
        this.gqam_gascenario = gqam_gascenario;
    }
    public GRM_SchedulableResource getGrm_schedulableresource() {
        return grm_schedulableresource;
    }

    public void setGrm_schedulableresource(GRM_SchedulableResource grm_schedulableresource) {
        this.grm_schedulableresource = grm_schedulableresource;
    }
    public List<GQAM_GaRequestedService> getGqam_garequestedservices() {
        return gqam_garequestedservices;
    }

    public void addGqam_garequestedservice(Gqam_garequestedservice gqam_garequestedservice) {
        this.gqam_garequestedservices.add(gqam_garequestedservice);
    }
    public GQAM_GaScenario getGqam_gascenario() {
        return gqam_gascenario;
    }

    public void setGqam_gascenario(GQAM_GaScenario gqam_gascenario) {
        this.gqam_gascenario = gqam_gascenario;
    }

}