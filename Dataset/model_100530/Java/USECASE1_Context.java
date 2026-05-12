





import java.util.List;
import java.util.ArrayList;

public class USECASE1_Context  {






    private List<UseCase> usecases;




    private List<PostCondition> postconditions;




    private List<PreCondition> preconditions;


    public USECASE1_Context(
    ) {
        this.usecases = new ArrayList<>();
        this.postconditions = new ArrayList<>();
        this.preconditions = new ArrayList<>();
    }

    public USECASE1_Context(
        ArrayList<UseCase> usecases,        ArrayList<PostCondition> postconditions,        ArrayList<PreCondition> preconditions    ) {
        this.usecases = usecases;
        this.postconditions = postconditions;
        this.preconditions = preconditions;
    }


    public List<UseCase> getUsecases() {
        return usecases;
    }

    public void addUsecase(Usecase usecase) {
        this.usecases.add(usecase);
    }
    public List<PostCondition> getPostconditions() {
        return postconditions;
    }

    public void addPostcondition(Postcondition postcondition) {
        this.postconditions.add(postcondition);
    }
    public List<PreCondition> getPreconditions() {
        return preconditions;
    }

    public void addPrecondition(Precondition precondition) {
        this.preconditions.add(precondition);
    }

}