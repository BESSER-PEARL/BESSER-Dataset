





import java.util.List;
import java.util.ArrayList;

public class Maintenance_Team_Actor  {






    private Send_for_Repair_UseCase send_for_repair_usecase;


    public Maintenance_Team_Actor(
    ) {
    }



    public Send_for_Repair_UseCase getSend_for_repair_usecase() {
        return send_for_repair_usecase;
    }

    public void setSend_for_repair_usecase(Send_for_Repair_UseCase send_for_repair_usecase) {
        this.send_for_repair_usecase = send_for_repair_usecase;
    }

}