





import java.util.List;
import java.util.ArrayList;

public class useCase_Actor  {

    private String name;





    private useCase_UseCase usecase_usecase;


    public useCase_Actor(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public useCase_UseCase getUsecase_usecase() {
        return usecase_usecase;
    }

    public void setUsecase_usecase(useCase_UseCase usecase_usecase) {
        this.usecase_usecase = usecase_usecase;
    }

}