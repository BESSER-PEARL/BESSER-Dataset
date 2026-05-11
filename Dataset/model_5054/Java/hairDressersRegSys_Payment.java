




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class hairDressersRegSys_Payment  {

    private String AmountPaid;
    private String PaymentMethod;
    private LocalDate Date;





    private hairDressersRegSys_Invoice hairdressersregsys_invoice;




    private List<hairDressersRegSys_Invoice> hairdressersregsys_invoices;


    public hairDressersRegSys_Payment(
        String AmountPaid,        String PaymentMethod,        LocalDate Date    ) {
        this.AmountPaid = AmountPaid;
        this.PaymentMethod = PaymentMethod;
        this.Date = Date;
        this.hairdressersregsys_invoices = new ArrayList<>();
    }

    public hairDressersRegSys_Payment(
        String AmountPaid,        String PaymentMethod,        LocalDate Date        ArrayList<hairDressersRegSys_Invoice> hairdressersregsys_invoices    ) {
        this.AmountPaid = AmountPaid;
        this.PaymentMethod = PaymentMethod;
        this.Date = Date;
        this.hairdressersregsys_invoices = hairdressersregsys_invoices;
    }

    public String getAmountpaid() {
        return AmountPaid;
    }

    public void setAmountpaid(String AmountPaid) {
        this.AmountPaid = AmountPaid;
    }
    public String getPaymentmethod() {
        return PaymentMethod;
    }

    public void setPaymentmethod(String PaymentMethod) {
        this.PaymentMethod = PaymentMethod;
    }
    public LocalDate getDate() {
        return Date;
    }

    public void setDate(LocalDate Date) {
        this.Date = Date;
    }

    public hairDressersRegSys_Invoice getHairdressersregsys_invoice() {
        return hairdressersregsys_invoice;
    }

    public void setHairdressersregsys_invoice(hairDressersRegSys_Invoice hairdressersregsys_invoice) {
        this.hairdressersregsys_invoice = hairdressersregsys_invoice;
    }
    public List<hairDressersRegSys_Invoice> getHairdressersregsys_invoices() {
        return hairdressersregsys_invoices;
    }

    public void addHairdressersregsys_invoice(Hairdressersregsys_invoice hairdressersregsys_invoice) {
        this.hairdressersregsys_invoices.add(hairdressersregsys_invoice);
    }

}