





import java.util.List;
import java.util.ArrayList;

public class Bank_Accounting_Actor  {






    private Bank_Server_Side_Authentication_UseCase bank_server_side_authentication_usecase;


    public Bank_Accounting_Actor(
    ) {
    }



    public Bank_Server_Side_Authentication_UseCase getBank_server_side_authentication_usecase() {
        return bank_server_side_authentication_usecase;
    }

    public void setBank_server_side_authentication_usecase(Bank_Server_Side_Authentication_UseCase bank_server_side_authentication_usecase) {
        this.bank_server_side_authentication_usecase = bank_server_side_authentication_usecase;
    }

}