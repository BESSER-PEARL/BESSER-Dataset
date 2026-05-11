





import java.util.List;
import java.util.ArrayList;

public class restbehavior_Creator  {






    private restbehavior_CreateAction restbehavior_createaction;




    private List<restbehavior_Parameter> restbehavior_parameters;




    private restbehavior_BehaviorSpecification restbehavior_behaviorspecification;


    public restbehavior_Creator(
    ) {
        this.restbehavior_parameters = new ArrayList<>();
    }

    public restbehavior_Creator(
        ArrayList<restbehavior_Parameter> restbehavior_parameters    ) {
        this.restbehavior_parameters = restbehavior_parameters;
    }


    public restbehavior_CreateAction getRestbehavior_createaction() {
        return restbehavior_createaction;
    }

    public void setRestbehavior_createaction(restbehavior_CreateAction restbehavior_createaction) {
        this.restbehavior_createaction = restbehavior_createaction;
    }
    public List<restbehavior_Parameter> getRestbehavior_parameters() {
        return restbehavior_parameters;
    }

    public void addRestbehavior_parameter(Restbehavior_parameter restbehavior_parameter) {
        this.restbehavior_parameters.add(restbehavior_parameter);
    }
    public restbehavior_BehaviorSpecification getRestbehavior_behaviorspecification() {
        return restbehavior_behaviorspecification;
    }

    public void setRestbehavior_behaviorspecification(restbehavior_BehaviorSpecification restbehavior_behaviorspecification) {
        this.restbehavior_behaviorspecification = restbehavior_behaviorspecification;
    }

}