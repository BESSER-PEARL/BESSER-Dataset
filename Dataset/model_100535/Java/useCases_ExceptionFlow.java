





import java.util.List;
import java.util.ArrayList;

public class useCases_ExceptionFlow extends NamedFlow {

    private String condition;





    private useCases_UseCase usecases_usecase;


    public useCases_ExceptionFlow(
        String condition    ) {
        super(
        );
        this.condition = condition;
    }


    public String getCondition() {
        return condition;
    }

    public void setCondition(String condition) {
        this.condition = condition;
    }

    public useCases_UseCase getUsecases_usecase() {
        return usecases_usecase;
    }

    public void setUsecases_usecase(useCases_UseCase usecases_usecase) {
        this.usecases_usecase = usecases_usecase;
    }

}