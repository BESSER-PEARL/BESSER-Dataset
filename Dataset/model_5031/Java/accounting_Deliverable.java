




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class accounting_Deliverable  {

    private LocalDate dueDate;
    private float unitAmount;





    private accounting_Order accounting_order;




    private accounting_Order accounting_order;


    public accounting_Deliverable(
        LocalDate dueDate,        float unitAmount    ) {
        this.dueDate = dueDate;
        this.unitAmount = unitAmount;
    }


    public LocalDate getDuedate() {
        return dueDate;
    }

    public void setDuedate(LocalDate dueDate) {
        this.dueDate = dueDate;
    }
    public float getUnitamount() {
        return unitAmount;
    }

    public void setUnitamount(float unitAmount) {
        this.unitAmount = unitAmount;
    }

    public accounting_Order getAccounting_order() {
        return accounting_order;
    }

    public void setAccounting_order(accounting_Order accounting_order) {
        this.accounting_order = accounting_order;
    }
    public accounting_Order getAccounting_order() {
        return accounting_order;
    }

    public void setAccounting_order(accounting_Order accounting_order) {
        this.accounting_order = accounting_order;
    }

}