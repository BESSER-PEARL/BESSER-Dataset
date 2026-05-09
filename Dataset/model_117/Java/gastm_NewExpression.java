





import java.util.List;
import java.util.ArrayList;

public class gastm_NewExpression extends Expression {






    private List<gastm_ActualParameter> gastm_actualparameters;




    private gastm_TypeReference gastm_typereference;


    public gastm_NewExpression(
    ) {
        super(
        );
        this.gastm_actualparameters = new ArrayList<>();
    }

    public gastm_NewExpression(
        ArrayList<gastm_ActualParameter> gastm_actualparameters    ) {
        this.gastm_actualparameters = gastm_actualparameters;
    }


    public List<gastm_ActualParameter> getGastm_actualparameters() {
        return gastm_actualparameters;
    }

    public void addGastm_actualparameter(Gastm_actualparameter gastm_actualparameter) {
        this.gastm_actualparameters.add(gastm_actualparameter);
    }
    public gastm_TypeReference getGastm_typereference() {
        return gastm_typereference;
    }

    public void setGastm_typereference(gastm_TypeReference gastm_typereference) {
        this.gastm_typereference = gastm_typereference;
    }

}