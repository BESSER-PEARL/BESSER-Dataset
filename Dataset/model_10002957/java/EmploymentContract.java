





import java.util.List;
import java.util.ArrayList;

public class EmploymentContract  {

    private None salary_payment;
    private int number_hours_per_week;
    private None type_contract;



    public EmploymentContract(
        None salary_payment,        int number_hours_per_week,        None type_contract    ) {
        this.salary_payment = salary_payment;
        this.number_hours_per_week = number_hours_per_week;
        this.type_contract = type_contract;
    }


    public None getSalary_payment() {
        return salary_payment;
    }

    public void setSalary_payment(None salary_payment) {
        this.salary_payment = salary_payment;
    }
    public int getNumber_hours_per_week() {
        return number_hours_per_week;
    }

    public void setNumber_hours_per_week(int number_hours_per_week) {
        this.number_hours_per_week = number_hours_per_week;
    }
    public None getType_contract() {
        return type_contract;
    }

    public void setType_contract(None type_contract) {
        this.type_contract = type_contract;
    }


}