





import java.util.List;
import java.util.ArrayList;

public class Withdraw_Cash_Display_the_PIN_screen_UseCase  {






    private Withdraw_Cash_Bank_Server_Actor withdraw_cash_bank_server_actor;




    private Withdraw_Cash__Enter_the_PIN_UseCase withdraw_cash__enter_the_pin_usecase;


    public Withdraw_Cash_Display_the_PIN_screen_UseCase(
    ) {
    }



    public Withdraw_Cash_Bank_Server_Actor getWithdraw_cash_bank_server_actor() {
        return withdraw_cash_bank_server_actor;
    }

    public void setWithdraw_cash_bank_server_actor(Withdraw_Cash_Bank_Server_Actor withdraw_cash_bank_server_actor) {
        this.withdraw_cash_bank_server_actor = withdraw_cash_bank_server_actor;
    }
    public Withdraw_Cash__Enter_the_PIN_UseCase getWithdraw_cash__enter_the_pin_usecase() {
        return withdraw_cash__enter_the_pin_usecase;
    }

    public void setWithdraw_cash__enter_the_pin_usecase(Withdraw_Cash__Enter_the_PIN_UseCase withdraw_cash__enter_the_pin_usecase) {
        this.withdraw_cash__enter_the_pin_usecase = withdraw_cash__enter_the_pin_usecase;
    }

}