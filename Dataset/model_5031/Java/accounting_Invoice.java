




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class accounting_Invoice  {

    private LocalDate dueDate;
    private float unitAmount;
    private String id;
    private String state;
    private LocalDate invoiceDate;





    private accounting_Order accounting_order;




    private accounting_Order accounting_order;




    private accounting_Employee accounting_employee;


    public accounting_Invoice(
        LocalDate dueDate,        float unitAmount,        String id,        String state,        LocalDate invoiceDate    ) {
        this.dueDate = dueDate;
        this.unitAmount = unitAmount;
        this.id = id;
        this.state = state;
        this.invoiceDate = invoiceDate;
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
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public LocalDate getInvoicedate() {
        return invoiceDate;
    }

    public void setInvoicedate(LocalDate invoiceDate) {
        this.invoiceDate = invoiceDate;
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
    public accounting_Employee getAccounting_employee() {
        return accounting_employee;
    }

    public void setAccounting_employee(accounting_Employee accounting_employee) {
        this.accounting_employee = accounting_employee;
    }

}