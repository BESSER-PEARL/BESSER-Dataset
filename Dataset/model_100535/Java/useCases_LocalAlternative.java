





import java.util.List;
import java.util.ArrayList;

public class useCases_LocalAlternative extends StepAlternative {

    private String description;





    private useCases_UseCase usecases_usecase;




    private useCases_Condition usecases_condition;


    public useCases_LocalAlternative(
        String description    ) {
        super(
        );
        this.description = description;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public useCases_UseCase getUsecases_usecase() {
        return usecases_usecase;
    }

    public void setUsecases_usecase(useCases_UseCase usecases_usecase) {
        this.usecases_usecase = usecases_usecase;
    }
    public useCases_Condition getUsecases_condition() {
        return usecases_condition;
    }

    public void setUsecases_condition(useCases_Condition usecases_condition) {
        this.usecases_condition = usecases_condition;
    }

}