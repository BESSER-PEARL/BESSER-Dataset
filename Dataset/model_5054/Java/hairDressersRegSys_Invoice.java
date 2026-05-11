





import java.util.List;
import java.util.ArrayList;

public class hairDressersRegSys_Invoice  {

    private String Date;
    private int InvoiceNumber;
    private String Total;





    private hairDressersRegSys_Appointment hairdressersregsys_appointment;


    public hairDressersRegSys_Invoice(
        String Date,        int InvoiceNumber,        String Total    ) {
        this.Date = Date;
        this.InvoiceNumber = InvoiceNumber;
        this.Total = Total;
    }


    public String getDate() {
        return Date;
    }

    public void setDate(String Date) {
        this.Date = Date;
    }
    public int getInvoicenumber() {
        return InvoiceNumber;
    }

    public void setInvoicenumber(int InvoiceNumber) {
        this.InvoiceNumber = InvoiceNumber;
    }
    public String getTotal() {
        return Total;
    }

    public void setTotal(String Total) {
        this.Total = Total;
    }

    public hairDressersRegSys_Appointment getHairdressersregsys_appointment() {
        return hairdressersregsys_appointment;
    }

    public void setHairdressersregsys_appointment(hairDressersRegSys_Appointment hairdressersregsys_appointment) {
        this.hairdressersregsys_appointment = hairdressersregsys_appointment;
    }

}