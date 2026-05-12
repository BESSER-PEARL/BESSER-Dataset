





import java.util.List;
import java.util.ArrayList;

public class useCase_Uses  {

    private String multiplicity;
    private String name;





    private useCase_Actor usecase_actor;


    public useCase_Uses(
        String multiplicity,        String name    ) {
        this.multiplicity = multiplicity;
        this.name = name;
    }


    public String getMultiplicity() {
        return multiplicity;
    }

    public void setMultiplicity(String multiplicity) {
        this.multiplicity = multiplicity;
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