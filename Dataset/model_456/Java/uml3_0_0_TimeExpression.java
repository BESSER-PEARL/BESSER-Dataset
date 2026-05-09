





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_TimeExpression extends ValueSpecification {






    private uml3_0_0_ValueSpecification uml3_0_0_valuespecification;




    private List<uml3_0_0_Observation> uml3_0_0_observations;


    public uml3_0_0_TimeExpression(
    ) {
        super(
        );
        this.uml3_0_0_observations = new ArrayList<>();
    }

    public uml3_0_0_TimeExpression(
        ArrayList<uml3_0_0_Observation> uml3_0_0_observations    ) {
        this.uml3_0_0_observations = uml3_0_0_observations;
    }


    public uml3_0_0_ValueSpecification getUml3_0_0_valuespecification() {
        return uml3_0_0_valuespecification;
    }

    public void setUml3_0_0_valuespecification(uml3_0_0_ValueSpecification uml3_0_0_valuespecification) {
        this.uml3_0_0_valuespecification = uml3_0_0_valuespecification;
    }
    public List<uml3_0_0_Observation> getUml3_0_0_observations() {
        return uml3_0_0_observations;
    }

    public void addUml3_0_0_observation(Uml3_0_0_observation uml3_0_0_observation) {
        this.uml3_0_0_observations.add(uml3_0_0_observation);
    }

}