





import java.util.List;
import java.util.ArrayList;

public class Payment  {

    private String Type_of_payment;





    private Money_Dispenser money_dispenser;




    private Cleaning_Management cleaning_management;




    private Primary_Info primary_info;




    private User user;


    public Payment(
        String Type_of_payment    ) {
        this.Type_of_payment = Type_of_payment;
    }


    public String getType_of_payment() {
        return Type_of_payment;
    }

    public void setType_of_payment(String Type_of_payment) {
        this.Type_of_payment = Type_of_payment;
    }

    public Money_Dispenser getMoney_dispenser() {
        return money_dispenser;
    }

    public void setMoney_dispenser(Money_Dispenser money_dispenser) {
        this.money_dispenser = money_dispenser;
    }
    public Cleaning_Management getCleaning_management() {
        return cleaning_management;
    }

    public void setCleaning_management(Cleaning_Management cleaning_management) {
        this.cleaning_management = cleaning_management;
    }
    public Primary_Info getPrimary_info() {
        return primary_info;
    }

    public void setPrimary_info(Primary_Info primary_info) {
        this.primary_info = primary_info;
    }
    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}