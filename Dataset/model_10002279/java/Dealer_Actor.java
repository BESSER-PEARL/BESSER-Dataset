





import java.util.List;
import java.util.ArrayList;

public class Dealer_Actor  {






    private Enquire_for_Cars_UseCase enquire_for_cars_usecase;




    private Send_for_Repair_UseCase send_for_repair_usecase;




    private Purchase_Car_UseCase purchase_car_usecase;


    public Dealer_Actor(
    ) {
    }



    public Enquire_for_Cars_UseCase getEnquire_for_cars_usecase() {
        return enquire_for_cars_usecase;
    }

    public void setEnquire_for_cars_usecase(Enquire_for_Cars_UseCase enquire_for_cars_usecase) {
        this.enquire_for_cars_usecase = enquire_for_cars_usecase;
    }
    public Send_for_Repair_UseCase getSend_for_repair_usecase() {
        return send_for_repair_usecase;
    }

    public void setSend_for_repair_usecase(Send_for_Repair_UseCase send_for_repair_usecase) {
        this.send_for_repair_usecase = send_for_repair_usecase;
    }
    public Purchase_Car_UseCase getPurchase_car_usecase() {
        return purchase_car_usecase;
    }

    public void setPurchase_car_usecase(Purchase_Car_UseCase purchase_car_usecase) {
        this.purchase_car_usecase = purchase_car_usecase;
    }

}