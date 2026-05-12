





import java.util.List;
import java.util.ArrayList;

public class Patient_Actor  {






    private Check_for_Appointments_UseCase check_for_appointments_usecase;


    public Patient_Actor(
    ) {
    }



    public Check_for_Appointments_UseCase getCheck_for_appointments_usecase() {
        return check_for_appointments_usecase;
    }

    public void setCheck_for_appointments_usecase(Check_for_Appointments_UseCase check_for_appointments_usecase) {
        this.check_for_appointments_usecase = check_for_appointments_usecase;
    }

}