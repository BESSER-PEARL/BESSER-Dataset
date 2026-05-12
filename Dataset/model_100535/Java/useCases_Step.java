





import java.util.List;
import java.util.ArrayList;

public class useCases_Step  {

    private String name;
    private String description;
    private String label;





    private useCases_UseCase usecases_usecase;




    private useCases_Flow usecases_flow;




    private useCases_Screen usecases_screen;




    private useCases_Actor usecases_actor;


    public useCases_Step(
        String name,        String description,        String label    ) {
        this.name = name;
        this.description = description;
        this.label = label;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public useCases_UseCase getUsecases_usecase() {
        return usecases_usecase;
    }

    public void setUsecases_usecase(useCases_UseCase usecases_usecase) {
        this.usecases_usecase = usecases_usecase;
    }
    public useCases_Flow getUsecases_flow() {
        return usecases_flow;
    }

    public void setUsecases_flow(useCases_Flow usecases_flow) {
        this.usecases_flow = usecases_flow;
    }
    public useCases_Screen getUsecases_screen() {
        return usecases_screen;
    }

    public void setUsecases_screen(useCases_Screen usecases_screen) {
        this.usecases_screen = usecases_screen;
    }
    public useCases_Actor getUsecases_actor() {
        return usecases_actor;
    }

    public void setUsecases_actor(useCases_Actor usecases_actor) {
        this.usecases_actor = usecases_actor;
    }

}