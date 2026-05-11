




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class accounting_Invoice  {

    private String id;
    private float unitAmount;
    private LocalDate invoiceDate;
    private String state;





    private accounting_Order accounting_order;




    private accounting_Order accounting_order;


    public accounting_Invoice(
        String id,        float unitAmount,        LocalDate invoiceDate,        String state    ) {
        this.id = id;
        this.unitAmount = unitAmount;
        this.invoiceDate = invoiceDate;
        this.state = state;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public float getUnitamount() {
        return unitAmount;
    }

    public void setUnitamount(float unitAmount) {
        this.unitAmount = unitAmount;
    }
    public LocalDate getInvoicedate() {
        return invoiceDate;
    }

    public void setInvoicedate(LocalDate invoiceDate) {
        this.invoiceDate = invoiceDate;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
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