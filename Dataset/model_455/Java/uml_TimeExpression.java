





import java.util.List;
import java.util.ArrayList;

public class uml_TimeExpression extends ValueSpecification {






    private List<uml_Observation> uml_observations;




    private uml_ValueSpecification uml_valuespecification;


    public uml_TimeExpression(
    ) {
        super(
        );
        this.uml_observations = new ArrayList<>();
    }

    public uml_TimeExpression(
        ArrayList<uml_Observation> uml_observations    ) {
        this.uml_observations = uml_observations;
    }


    public List<uml_Observation> getUml_observations() {
        return uml_observations;
    }

    public void addUml_observation(Uml_observation uml_observation) {
        this.uml_observations.add(uml_observation);
    }
    public uml_ValueSpecification getUml_valuespecification() {
        return uml_valuespecification;
    }

    public void setUml_valuespecification(uml_ValueSpecification uml_valuespecification) {
        this.uml_valuespecification = uml_valuespecification;
    }

}