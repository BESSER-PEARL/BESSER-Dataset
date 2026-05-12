





import java.util.List;
import java.util.ArrayList;

public class Bank_Mobile_Money_Agent_Actor  {






    private Confirm_Payment_UseCase confirm_payment_usecase;


    public Bank_Mobile_Money_Agent_Actor(
    ) {
    }



    public Confirm_Payment_UseCase getConfirm_payment_usecase() {
        return confirm_payment_usecase;
    }

    public void setConfirm_payment_usecase(Confirm_Payment_UseCase confirm_payment_usecase) {
        this.confirm_payment_usecase = confirm_payment_usecase;
    }

}