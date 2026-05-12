





import java.util.List;
import java.util.ArrayList;

public class USECASEUML_Goal  {






    private List<UseCase> usecases;


    public USECASEUML_Goal(
    ) {
        this.usecases = new ArrayList<>();
    }

    public USECASEUML_Goal(
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