





import java.util.List;
import java.util.ArrayList;

public class UseCaseDSL_Step  {

    private String name;
    private String label;





    private UseCaseDSL_Step usecasedsl_step;




    private UseCaseDSL_Flow usecasedsl_flow;


    public UseCaseDSL_Step(
        String name,        String label    ) {
        this.name = name;
        this.label = label;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public UseCaseDSL_Step getUsecasedsl_step() {
        return usecasedsl_step;
    }

    public void setUsecasedsl_step(UseCaseDSL_Step usecasedsl_step) {
        this.usecasedsl_step = usecasedsl_step;
    }
    public UseCaseDSL_Flow getUsecasedsl_flow() {
        return usecasedsl_flow;
    }

    public void setUsecasedsl_flow(UseCaseDSL_Flow usecasedsl_flow) {
        this.usecasedsl_flow = usecasedsl_flow;
    }

}