





import java.util.List;
import java.util.ArrayList;

public class Administrator_Actor  {






    private Make_requests_to_administrator_UseCase make_requests_to_administrator_usecase;




    private Logging_into_program_UseCase1 logging_into_program_usecase1;


    public Administrator_Actor(
    ) {
    }



    public Make_requests_to_administrator_UseCase getMake_requests_to_administrator_usecase() {
        return make_requests_to_administrator_usecase;
    }

    public void setMake_requests_to_administrator_usecase(Make_requests_to_administrator_UseCase make_requests_to_administrator_usecase) {
        this.make_requests_to_administrator_usecase = make_requests_to_administrator_usecase;
    }
    public Logging_into_program_UseCase1 getLogging_into_program_usecase1() {
        return logging_into_program_usecase1;
    }

    public void setLogging_into_program_usecase1(Logging_into_program_UseCase1 logging_into_program_usecase1) {
        this.logging_into_program_usecase1 = logging_into_program_usecase1;
    }

}