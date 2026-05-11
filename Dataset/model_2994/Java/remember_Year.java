





import java.util.List;
import java.util.ArrayList;

public class remember_Year  {

    private int year;





    private remember_InvoiceSpecification remember_invoicespecification;




    private List<remember_InvoiceSpecification> remember_invoicespecifications;


    public remember_Year(
        int year    ) {
        this.year = year;
        this.remember_invoicespecifications = new ArrayList<>();
    }

    public remember_Year(
        int year        ArrayList<remember_InvoiceSpecification> remember_invoicespecifications    ) {
        this.year = year;
        this.remember_invoicespecifications = remember_invoicespecifications;
    }

    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }

    public remember_InvoiceSpecification getRemember_invoicespecification() {
        return remember_invoicespecification;
    }

    public void setRemember_invoicespecification(remember_InvoiceSpecification remember_invoicespecification) {
        this.remember_invoicespecification = remember_invoicespecification;
    }
    public List<remember_InvoiceSpecification> getRemember_invoicespecifications() {
        return remember_invoicespecifications;
    }

    public void addRemember_invoicespecification(Remember_invoicespecification remember_invoicespecification) {
        this.remember_invoicespecifications.add(remember_invoicespecification);
    }

}