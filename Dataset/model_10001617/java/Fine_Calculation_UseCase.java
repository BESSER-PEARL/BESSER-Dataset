





import java.util.List;
import java.util.ArrayList;

public class Fine_Calculation_UseCase  {






    private Reminder_System_UseCase reminder_system_usecase;




    private Librarian_Actor librarian_actor;


    public Fine_Calculation_UseCase(
    ) {
    }



    public Reminder_System_UseCase getReminder_system_usecase() {
        return reminder_system_usecase;
    }

    public void setReminder_system_usecase(Reminder_System_UseCase reminder_system_usecase) {
        this.reminder_system_usecase = reminder_system_usecase;
    }
    public Librarian_Actor getLibrarian_actor() {
        return librarian_actor;
    }

    public void setLibrarian_actor(Librarian_Actor librarian_actor) {
        this.librarian_actor = librarian_actor;
    }

}