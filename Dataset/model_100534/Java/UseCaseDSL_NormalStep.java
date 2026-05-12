





import java.util.List;
import java.util.ArrayList;

public class UseCaseDSL_NormalStep extends Step {

    private String customStepType;





    private UseCaseDSL_Actor usecasedsl_actor;


    public UseCaseDSL_NormalStep(
        String customStepType    ) {
        super(
        );
        this.customStepType = customStepType;
    }


    public String getCustomsteptype() {
        return customStepType;
    }

    public void setCustomsteptype(String customStepType) {
        this.customStepType = customStepType;
    }

    public UseCaseDSL_Actor getUsecasedsl_actor() {
        return usecasedsl_actor;
    }

    public void setUsecasedsl_actor(UseCaseDSL_Actor usecasedsl_actor) {
        this.usecasedsl_actor = usecasedsl_actor;
    }

}