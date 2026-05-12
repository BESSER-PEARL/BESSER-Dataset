





import java.util.List;
import java.util.ArrayList;

public class HSM_AssociationDataStateBase  {






    private List<StateBase> statebases;




    private StateDataRelation statedatarelation;




    private List<DataVar> datavars;


    public HSM_AssociationDataStateBase(
    ) {
        this.statebases = new ArrayList<>();
        this.datavars = new ArrayList<>();
    }

    public HSM_AssociationDataStateBase(
        ArrayList<StateBase> statebases,        ArrayList<DataVar> datavars    ) {
        this.statebases = statebases;
        this.datavars = datavars;
    }


    public List<StateBase> getStatebases() {
        return statebases;
    }

    public void addStatebase(Statebase statebase) {
        this.statebases.add(statebase);
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

}