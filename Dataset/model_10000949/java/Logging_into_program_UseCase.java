





import java.util.List;
import java.util.ArrayList;

public class Logging_into_program_UseCase  {






    private Check_black_list_requests_UseCase check_black_list_requests_usecase;




    private Register_pets__physical_characteristics_UseCase register_pets__physical_characteristics_usecase;




    private Administrator_Actor administrator_actor;


    public Logging_into_program_UseCase(
    ) {
    }



    public Check_black_list_requests_UseCase getCheck_black_list_requests_usecase() {
        return check_black_list_requests_usecase;
    }

    public void setCheck_black_list_requests_usecase(Check_black_list_requests_UseCase check_black_list_requests_usecase) {
        this.check_black_list_requests_usecase = check_black_list_requests_usecase;
    }
    public Register_pets__physical_characteristics_UseCase getRegister_pets__physical_characteristics_usecase() {
        return register_pets__physical_characteristics_usecase;
    }

    public void setRegister_pets__physical_characteristics_usecase(Register_pets__physical_characteristics_UseCase register_pets__physical_characteristics_usecase) {
        this.register_pets__physical_characteristics_usecase = register_pets__physical_characteristics_usecase;
    }
    public Administrator_Actor getAdministrator_actor() {
        return administrator_actor;
    }

    public void setAdministrator_actor(Administrator_Actor administrator_actor) {
        this.administrator_actor = administrator_actor;
    }

}