





import java.util.List;
import java.util.ArrayList;

public class Create_new_administrators_UseCase  {






    private Logging_into_program_UseCase logging_into_program_usecase;


    public Create_new_administrators_UseCase(
    ) {
    }



    public Logging_into_program_UseCase getLogging_into_program_usecase() {
        return logging_into_program_usecase;
    }

    public void setLogging_into_program_usecase(Logging_into_program_UseCase logging_into_program_usecase) {
        this.logging_into_program_usecase = logging_into_program_usecase;
    }

}