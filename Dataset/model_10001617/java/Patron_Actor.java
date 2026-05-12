





import java.util.List;
import java.util.ArrayList;

public class Patron_Actor  {






    private Reminder_System_UseCase reminder_system_usecase;




    private Check_In_UseCase check_in_usecase;




    private Check_out_UseCase check_out_usecase;


    public Patron_Actor(
    ) {
    }



    public Reminder_System_UseCase getReminder_system_usecase() {
        return reminder_system_usecase;
    }

    public void setReminder_system_usecase(Reminder_System_UseCase reminder_system_usecase) {
        this.reminder_system_usecase = reminder_system_usecase;
    }
    public Check_In_UseCase getCheck_in_usecase() {
        return check_in_usecase;
    }

    public void setCheck_in_usecase(Check_In_UseCase check_in_usecase) {
        this.check_in_usecase = check_in_usecase;
    }
    public Check_out_UseCase getCheck_out_usecase() {
        return check_out_usecase;
    }

    public void setCheck_out_usecase(Check_out_UseCase check_out_usecase) {
        this.check_out_usecase = check_out_usecase;
    }

}