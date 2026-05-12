





import java.util.List;
import java.util.ArrayList;

public class useCase_Case  {

    private String name;





    private List<useCase_Includes> usecase_includess;




    private List<useCase_Extends> usecase_extendss;




    private useCase_Subsystem usecase_subsystem;


    public useCase_Case(
        String name    ) {
        this.name = name;
        this.usecase_includess = new ArrayList<>();
        this.usecase_extendss = new ArrayList<>();
    }

    public useCase_Case(
        String name        ArrayList<useCase_Includes> usecase_includess,        ArrayList<useCase_Extends> usecase_extendss    ) {
        this.name = name;
        this.usecase_includess = usecase_includess;
        this.usecase_extendss = usecase_extendss;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<useCase_Includes> getUsecase_includess() {
        return usecase_includess;
    }

    public void addUsecase_includes(Usecase_includes usecase_includes) {
        this.usecase_includess.add(usecase_includes);
    }
    public List<useCase_Extends> getUsecase_extendss() {
        return usecase_extendss;
    }

    public void addUsecase_extends(Usecase_extends usecase_extends) {
        this.usecase_extendss.add(usecase_extends);
    }
    public useCase_Subsystem getUsecase_subsystem() {
        return usecase_subsystem;
    }

    public void setUsecase_subsystem(useCase_Subsystem usecase_subsystem) {
        this.usecase_subsystem = usecase_subsystem;
    }

}