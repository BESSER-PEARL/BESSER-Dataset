




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Classes_Charge  {

    private int amount;
    private String chargeType;
    private LocalDate date;





    private Classes_Bill classes_bill;


    public Classes_Charge(
        int amount,        String chargeType,        LocalDate date    ) {
        this.amount = amount;
        this.chargeType = chargeType;
        this.date = date;
    }


    public int getAmount() {
        return amount;
    }

    public void setAmount(int amount) {
        this.amount = amount;
    }
    public String getChargetype() {
        return chargeType;
    }

    public void setChargetype(String chargeType) {
        this.chargeType = chargeType;
    }
    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }

    public Classes_Bill getClasses_bill() {
        return classes_bill;
    }

    public void setClasses_bill(Classes_Bill classes_bill) {
        this.classes_bill = classes_bill;
    }

}