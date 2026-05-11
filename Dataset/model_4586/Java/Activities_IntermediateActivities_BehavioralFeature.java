





import java.util.List;
import java.util.ArrayList;

public class Activities_IntermediateActivities_BehavioralFeature extends FundamentalActivities_Namespace, IntermediateActivities_Feature {






    private List<ParameterSet> parametersets;


    public Activities_IntermediateActivities_BehavioralFeature(
    ) {
        super(
        );
        this.parametersets = new ArrayList<>();
    }

    public Activities_IntermediateActivities_BehavioralFeature(
        ArrayList<ParameterSet> parametersets    ) {
        this.parametersets = parametersets;
    }


    public List<ParameterSet> getParametersets() {
        return parametersets;
    }

    public void addParameterset(Parameterset parameterset) {
        this.parametersets.add(parameterset);
    }

}