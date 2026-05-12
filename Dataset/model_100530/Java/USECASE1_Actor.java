





import java.util.List;
import java.util.ArrayList;

public class USECASE1_Actor  {






    private List<UseCase> usecases;


    public USECASE1_Actor(
    ) {
        this.usecases = new ArrayList<>();
    }

    public USECASE1_Actor(
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