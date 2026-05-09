





import java.util.List;
import java.util.ArrayList;

public class uml_Duration extends ValueSpecification {






    private uml_ValueSpecification uml_valuespecification;




    private List<uml_Observation> uml_observations;


    public uml_Duration(
    ) {
        super(
        );
        this.uml_observations = new ArrayList<>();
    }

    public uml_Duration(
        ArrayList<uml_Observation> uml_observations    ) {
        this.uml_observations = uml_observations;
    }


    public uml_ValueSpecification getUml_valuespecification() {
        return uml_valuespecification;
    }

    public void setUml_valuespecification(uml_ValueSpecification uml_valuespecification) {
        this.uml_valuespecification = uml_valuespecification;
    }
    public List<uml_Observation> getUml_observations() {
        return uml_observations;
    }

    public void addUml_observation(Uml_observation uml_observation) {
        this.uml_observations.add(uml_observation);
    }

}