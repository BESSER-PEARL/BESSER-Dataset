





import java.util.List;
import java.util.ArrayList;

public class urml_usecase_Actor extends Asset {






    private List<UseCase> usecases;


    public urml_usecase_Actor(
    ) {
        super(
        );
        this.usecases = new ArrayList<>();
    }

    public urml_usecase_Actor(
        ArrayList<UseCase> usecases    ) {
        this.usecases = usecases;
    }


    public List<UseCase> getUsecases() {
        return usecases;
    }

    public void addUsecase(Usecase usecase) {
        this.usecases.add(usecase);
    }

}