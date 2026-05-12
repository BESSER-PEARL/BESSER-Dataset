





import java.util.List;
import java.util.ArrayList;

public class Bank_System_Actor  {






    private Shopping_System_Payment_UseCase shopping_system_payment_usecase;


    public Bank_System_Actor(
    ) {
    }



    public Shopping_System_Payment_UseCase getShopping_system_payment_usecase() {
        return shopping_system_payment_usecase;
    }

    public void setShopping_system_payment_usecase(Shopping_System_Payment_UseCase shopping_system_payment_usecase) {
        this.shopping_system_payment_usecase = shopping_system_payment_usecase;
    }

}