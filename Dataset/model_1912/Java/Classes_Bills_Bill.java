




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Classes_Bills_Bill  {

    private String bookable;
    private LocalDate issueDate;
    private LocalDate paymentDate;
    private String isPaid;
    private String services;
    private String id;
    private String items;
    private String paymentType;
    private float totalAmount;



    public Classes_Bills_Bill(
        String bookable,        LocalDate issueDate,        LocalDate paymentDate,        String isPaid,        String services,        String id,        String items,        String paymentType,        float totalAmount    ) {
        this.bookable = bookable;
        this.issueDate = issueDate;
        this.paymentDate = paymentDate;
        this.isPaid = isPaid;
        this.services = services;
        this.id = id;
        this.items = items;
        this.paymentType = paymentType;
        this.totalAmount = totalAmount;
    }


    public String getBookable() {
        return bookable;
    }

    public void setBookable(String bookable) {
        this.bookable = bookable;
    }
    public LocalDate getIssuedate() {
        return issueDate;
    }

    public void setIssuedate(LocalDate issueDate) {
        this.issueDate = issueDate;
    }
    public LocalDate getPaymentdate() {
        return paymentDate;
    }

    public void setPaymentdate(LocalDate paymentDate) {
        this.paymentDate = paymentDate;
    }
    public String getIspaid() {
        return isPaid;
    }

    public void setIspaid(String isPaid) {
        this.isPaid = isPaid;
    }
    public String getServices() {
        return services;
    }

    public void setServices(String services) {
        this.services = services;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getItems() {
        return items;
    }

    public void setItems(String items) {
        this.items = items;
    }
    public String getPaymenttype() {
        return paymentType;
    }

    public void setPaymenttype(String paymentType) {
        this.paymentType = paymentType;
    }
    public float getTotalamount() {
        return totalAmount;
    }

    public void setTotalamount(float totalAmount) {
        this.totalAmount = totalAmount;
    }


}