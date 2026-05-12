





import java.util.List;
import java.util.ArrayList;

public class Receptionist_Actor  {






    private Check_out_Guest_UseCase check_out_guest_usecase;




    private Check_in_Guest_UseCase check_in_guest_usecase;


    public Receptionist_Actor(
    ) {
    }



    public Check_out_Guest_UseCase getCheck_out_guest_usecase() {
        return check_out_guest_usecase;
    }

    public void setCheck_out_guest_usecase(Check_out_Guest_UseCase check_out_guest_usecase) {
        this.check_out_guest_usecase = check_out_guest_usecase;
    }
    public Check_in_Guest_UseCase getCheck_in_guest_usecase() {
        return check_in_guest_usecase;
    }

    public void setCheck_in_guest_usecase(Check_in_Guest_UseCase check_in_guest_usecase) {
        this.check_in_guest_usecase = check_in_guest_usecase;
    }

}