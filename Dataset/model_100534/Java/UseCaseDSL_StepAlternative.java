





import java.util.List;
import java.util.ArrayList;

public class UseCaseDSL_StepAlternative  {

    private String condition;





    private UseCaseDSL_Step usecasedsl_step;




    private UseCaseDSL_NormalStep usecasedsl_normalstep;


    public UseCaseDSL_StepAlternative(
        String condition    ) {
        this.condition = condition;
    }


    public String getCondition() {
        return condition;
    }

    public void setCondition(String condition) {
        this.condition = condition;
    }

    public UseCaseDSL_Step getUsecasedsl_step() {
        return usecasedsl_step;
    }

    public void setUsecasedsl_step(UseCaseDSL_Step usecasedsl_step) {
        this.usecasedsl_step = usecasedsl_step;
    }
    public UseCaseDSL_NormalStep getUsecasedsl_normalstep() {
        return usecasedsl_normalstep;
    }

    public void setUsecasedsl_normalstep(UseCaseDSL_NormalStep usecasedsl_normalstep) {
        this.usecasedsl_normalstep = usecasedsl_normalstep;
    }

}