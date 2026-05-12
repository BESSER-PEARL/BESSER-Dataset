





import java.util.List;
import java.util.ArrayList;

public class UseCase_Include  {






    private List<UseCase> usecases;


    public UseCase_Include(
    ) {
        this.usecases = new ArrayList<>();
    }

    public UseCase_Include(
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