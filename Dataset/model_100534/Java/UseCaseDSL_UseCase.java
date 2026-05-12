





import java.util.List;
import java.util.ArrayList;

public class UseCaseDSL_UseCase  {

    private String preConditions;
    private String description;
    private String postcondition;
    private String name;





    private UseCaseDSL_LocalAlternative usecasedsl_localalternative;




    private UseCaseDSL_UseCase usecasedsl_usecase;




    private UseCaseDSL_Step usecasedsl_step;




    private List<UseCaseDSL_Flow> usecasedsl_flows;


    public UseCaseDSL_UseCase(
        String preConditions,        String description,        String postcondition,        String name    ) {
        this.preConditions = preConditions;
        this.description = description;
        this.postcondition = postcondition;
        this.name = name;
        this.usecasedsl_flows = new ArrayList<>();
    }

    public UseCaseDSL_UseCase(
        String preConditions,        String description,        String postcondition,        String name        ArrayList<UseCaseDSL_Flow> usecasedsl_flows    ) {
        this.preConditions = preConditions;
        this.description = description;
        this.postcondition = postcondition;
        this.name = name;
        this.usecasedsl_flows = usecasedsl_flows;
    }

    public String getPreconditions() {
        return preConditions;
    }

    public void setPreconditions(String preConditions) {
        this.preConditions = preConditions;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getPostcondition() {
        return postcondition;
    }

    public void setPostcondition(String postcondition) {
        this.postcondition = postcondition;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public UseCaseDSL_LocalAlternative getUsecasedsl_localalternative() {
        return usecasedsl_localalternative;
    }

    public void setUsecasedsl_localalternative(UseCaseDSL_LocalAlternative usecasedsl_localalternative) {
        this.usecasedsl_localalternative = usecasedsl_localalternative;
    }
    public UseCaseDSL_UseCase getUsecasedsl_usecase() {
        return usecasedsl_usecase;
    }

    public void setUsecasedsl_usecase(UseCaseDSL_UseCase usecasedsl_usecase) {
        this.usecasedsl_usecase = usecasedsl_usecase;
    }
    public UseCaseDSL_Step getUsecasedsl_step() {
        return usecasedsl_step;
    }

    public void setUsecasedsl_step(UseCaseDSL_Step usecasedsl_step) {
        this.usecasedsl_step = usecasedsl_step;
    }
    public List<UseCaseDSL_Flow> getUsecasedsl_flows() {
        return usecasedsl_flows;
    }

    public void addUsecasedsl_flow(Usecasedsl_flow usecasedsl_flow) {
        this.usecasedsl_flows.add(usecasedsl_flow);
    }

}