





import java.util.List;
import java.util.ArrayList;

public class metamodel_Group extends Actuator {






    private List<metamodel_DifferentialWheel> metamodel_differentialwheels;


    public metamodel_Group(
    ) {
        super(
        );
        this.metamodel_differentialwheels = new ArrayList<>();
    }

    public metamodel_Group(
        ArrayList<metamodel_DifferentialWheel> metamodel_differentialwheels    ) {
        this.metamodel_differentialwheels = metamodel_differentialwheels;
    }


    public List<metamodel_DifferentialWheel> getMetamodel_differentialwheels() {
        return metamodel_differentialwheels;
    }

    public void addMetamodel_differentialwheel(Metamodel_differentialwheel metamodel_differentialwheel) {
        this.metamodel_differentialwheels.add(metamodel_differentialwheel);
    }

}