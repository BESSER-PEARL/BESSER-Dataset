





import java.util.List;
import java.util.ArrayList;

public class UseCaseDSL_NamedFlow extends Flow {

    private String name;





    private UseCaseDSL_AlternativeFlowAlternative usecasedsl_alternativeflowalternative;


    public UseCaseDSL_NamedFlow(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public UseCaseDSL_AlternativeFlowAlternative getUsecasedsl_alternativeflowalternative() {
        return usecasedsl_alternativeflowalternative;
    }

    public void setUsecasedsl_alternativeflowalternative(UseCaseDSL_AlternativeFlowAlternative usecasedsl_alternativeflowalternative) {
        this.usecasedsl_alternativeflowalternative = usecasedsl_alternativeflowalternative;
    }

}