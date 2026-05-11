




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class model_Voucher extends IEntity {

    private LocalDate voucherDate;
    private String doNotBook;
    private String documentNumber;
    private String totalValue;
    private String discounted;
    private String voucherType;
    private String paidValue;
    private String voucherNumber;



    public model_Voucher(
        LocalDate voucherDate,        String doNotBook,        String documentNumber,        String totalValue,        String discounted,        String voucherType,        String paidValue,        String voucherNumber    ) {
        super(
        );
        this.voucherDate = voucherDate;
        this.doNotBook = doNotBook;
        this.documentNumber = documentNumber;
        this.totalValue = totalValue;
        this.discounted = discounted;
        this.voucherType = voucherType;
        this.paidValue = paidValue;
        this.voucherNumber = voucherNumber;
    }


    public LocalDate getVoucherdate() {
        return voucherDate;
    }

    public void setVoucherdate(LocalDate voucherDate) {
        this.voucherDate = voucherDate;
    }
    public String getDonotbook() {
        return doNotBook;
    }

    public void setDonotbook(String doNotBook) {
        this.doNotBook = doNotBook;
    }
    public String getDocumentnumber() {
        return documentNumber;
    }

    public void setDocumentnumber(String documentNumber) {
        this.documentNumber = documentNumber;
    }
    public String getTotalvalue() {
        return totalValue;
    }

    public void setTotalvalue(String totalValue) {
        this.totalValue = totalValue;
    }
    public String getDiscounted() {
        return discounted;
    }

    public void setDiscounted(String discounted) {
        this.discounted = discounted;
    }
    public String getVouchertype() {
        return voucherType;
    }

    public void setVouchertype(String voucherType) {
        this.voucherType = voucherType;
    }
    public String getPaidvalue() {
        return paidValue;
    }

    public void setPaidvalue(String paidValue) {
        this.paidValue = paidValue;
    }
    public String getVouchernumber() {
        return voucherNumber;
    }

    public void setVouchernumber(String voucherNumber) {
        this.voucherNumber = voucherNumber;
    }


}