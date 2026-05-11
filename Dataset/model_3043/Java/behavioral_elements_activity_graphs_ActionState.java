





import java.util.List;
import java.util.ArrayList;

public class behavioral_elements_activity_graphs_ActionState extends SimpleState {

    private String isDynamic;





    private Multiplicity_ multiplicity_;


    public behavioral_elements_activity_graphs_ActionState(
        String isDynamic    ) {
        super(
        );
        this.isDynamic = isDynamic;
    }


    public String getIsdynamic() {
        return isDynamic;
    }

    public void setIsdynamic(String isDynamic) {
        this.isDynamic = isDynamic;
    }

    public Multiplicity_ getMultiplicity_() {
        return multiplicity_;
    }

    public void setMultiplicity_(Multiplicity_ multiplicity_) {
        this.multiplicity_ = multiplicity_;
    }

}