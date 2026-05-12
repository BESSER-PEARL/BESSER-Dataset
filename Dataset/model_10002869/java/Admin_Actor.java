





import java.util.List;
import java.util.ArrayList;

public class Admin_Actor  {






    private Update_Calendar_UseCase update_calendar_usecase;




    private CreateUser_UseCase createuser_usecase;


    public Admin_Actor(
    ) {
    }



    public Update_Calendar_UseCase getUpdate_calendar_usecase() {
        return update_calendar_usecase;
    }

    public void setUpdate_calendar_usecase(Update_Calendar_UseCase update_calendar_usecase) {
        this.update_calendar_usecase = update_calendar_usecase;
    }
    public CreateUser_UseCase getCreateuser_usecase() {
        return createuser_usecase;
    }

    public void setCreateuser_usecase(CreateUser_UseCase createuser_usecase) {
        this.createuser_usecase = createuser_usecase;
    }

}