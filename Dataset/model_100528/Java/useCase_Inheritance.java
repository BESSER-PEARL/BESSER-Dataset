





import java.util.List;
import java.util.ArrayList;

public class useCase_Inheritance  {

    private String name;





    private useCase_Actor usecase_actor;


    public useCase_Inheritance(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public useCase_Actor getUsecase_actor() {
        return usecase_actor;
    }

    public void setUsecase_actor(useCase_Actor usecase_actor) {
        this.usecase_actor = usecase_actor;
    }

}