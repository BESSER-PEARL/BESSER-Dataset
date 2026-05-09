





import java.util.List;
import java.util.ArrayList;

public class analysis_partitioning_ComCostPartition  {

    private String externalCost;
    private String internalCost;





    private List<ActorToLongMap> actortolongmaps;




    private List<ActorToLongMap> actortolongmaps;


    public analysis_partitioning_ComCostPartition(
        String externalCost,        String internalCost    ) {
        this.externalCost = externalCost;
        this.internalCost = internalCost;
        this.actortolongmaps = new ArrayList<>();
        this.actortolongmaps = new ArrayList<>();
    }

    public analysis_partitioning_ComCostPartition(
        String externalCost,        String internalCost        ArrayList<ActorToLongMap> actortolongmaps,        ArrayList<ActorToLongMap> actortolongmaps    ) {
        this.externalCost = externalCost;
        this.internalCost = internalCost;
        this.actortolongmaps = actortolongmaps;
        this.actortolongmaps = actortolongmaps;
    }

    public String getExternalcost() {
        return externalCost;
    }

    public void setExternalcost(String externalCost) {
        this.externalCost = externalCost;
    }
    public String getInternalcost() {
        return internalCost;
    }

    public void setInternalcost(String internalCost) {
        this.internalCost = internalCost;
    }

    public List<ActorToLongMap> getActortolongmaps() {
        return actortolongmaps;
    }

    public void addActortolongmap(Actortolongmap actortolongmap) {
        this.actortolongmaps.add(actortolongmap);
    }
    public List<ActorToLongMap> getActortolongmaps() {
        return actortolongmaps;
    }

    public void addActortolongmap(Actortolongmap actortolongmap) {
        this.actortolongmaps.add(actortolongmap);
    }

}