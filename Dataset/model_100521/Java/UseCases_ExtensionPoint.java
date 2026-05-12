





import java.util.List;
import java.util.ArrayList;

public class UseCases_ExtensionPoint extends ModelElement {






    private List<UseCase> usecases;




    private List<Extend> extends;


    public UseCases_ExtensionPoint(
    ) {
        super(
        );
        this.usecases = new ArrayList<>();
        this.extends = new ArrayList<>();
    }

    public UseCases_ExtensionPoint(
        ArrayList<UseCase> usecases,        ArrayList<Extend> extends    ) {
        this.usecases = usecases;
        this.extends = extends;
    }


    public List<UseCase> getUsecases() {
        return usecases;
    }

    public void addUsecase(Usecase usecase) {
        this.usecases.add(usecase);
    }
    public List<Extend> getExtends() {
        return extends;
    }

    public void addExtend(Extend extend) {
        this.extends.add(extend);
    }

}