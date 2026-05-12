





import java.util.List;
import java.util.ArrayList;

public class useCase_ExtensionPoint  {

    private String name;





    private useCase_Case usecase_case;


    public useCase_ExtensionPoint(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public useCase_Case getUsecase_case() {
        return usecase_case;
    }

    public void setUsecase_case(useCase_Case usecase_case) {
        this.usecase_case = usecase_case;
    }

}