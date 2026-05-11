





import java.util.List;
import java.util.ArrayList;

public class diva_VariabilityModel extends ModelContainer {






    private diva_SimulationModel diva_simulationmodel;




    private diva_SimulationModel diva_simulationmodel;




    private List<diva_Constraint> diva_constraints;


    public diva_VariabilityModel(
    ) {
        super(
        );
        this.diva_constraints = new ArrayList<>();
    }

    public diva_VariabilityModel(
        ArrayList<diva_Constraint> diva_constraints    ) {
        this.diva_constraints = diva_constraints;
    }


    public diva_SimulationModel getDiva_simulationmodel() {
        return diva_simulationmodel;
    }

    public void setDiva_simulationmodel(diva_SimulationModel diva_simulationmodel) {
        this.diva_simulationmodel = diva_simulationmodel;
    }
    public diva_SimulationModel getDiva_simulationmodel() {
        return diva_simulationmodel;
    }

    public void setDiva_simulationmodel(diva_SimulationModel diva_simulationmodel) {
        this.diva_simulationmodel = diva_simulationmodel;
    }
    public List<diva_Constraint> getDiva_constraints() {
        return diva_constraints;
    }

    public void addDiva_constraint(Diva_constraint diva_constraint) {
        this.diva_constraints.add(diva_constraint);
    }

}