





import java.util.List;
import java.util.ArrayList;

public class HSM_AssociationDataStateBase  {






    private StateDataRelation statedatarelation;




    private List<DataVar> datavars;




    private List<StateBase> statebases;


    public HSM_AssociationDataStateBase(
    ) {
        this.datavars = new ArrayList<>();
        this.statebases = new ArrayList<>();
    }

    public HSM_AssociationDataStateBase(
        ArrayList<DataVar> datavars,        ArrayList<StateBase> statebases    ) {
        this.datavars = datavars;
        this.statebases = statebases;
    }


    public StateDataRelation getStatedatarelation() {
        return statedatarelation;
    }

    public void setStatedatarelation(StateDataRelation statedatarelation) {
        this.statedatarelation = statedatarelation;
    }
    public List<DataVar> getDatavars() {
        return datavars;
    }

    public void addDatavar(Datavar datavar) {
        this.datavars.add(datavar);
    }
    public List<StateBase> getStatebases() {
        return statebases;
    }

    public void addStatebase(Statebase statebase) {
        this.statebases.add(statebase);
    }

}