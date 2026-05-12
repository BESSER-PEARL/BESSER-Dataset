





import java.util.List;
import java.util.ArrayList;

public class Confirm_Payment_UseCase  {






    private Administrator_Actor administrator_actor;




    private Bank_Mobile_Money_Agent_Actor bank_mobile_money_agent_actor;


    public Confirm_Payment_UseCase(
    ) {
    }



    public Administrator_Actor getAdministrator_actor() {
        return administrator_actor;
    }

    public void setAdministrator_actor(Administrator_Actor administrator_actor) {
        this.administrator_actor = administrator_actor;
    }
    public Bank_Mobile_Money_Agent_Actor getBank_mobile_money_agent_actor() {
        return bank_mobile_money_agent_actor;
    }

    public void setBank_mobile_money_agent_actor(Bank_Mobile_Money_Agent_Actor bank_mobile_money_agent_actor) {
        this.bank_mobile_money_agent_actor = bank_mobile_money_agent_actor;
    }

}