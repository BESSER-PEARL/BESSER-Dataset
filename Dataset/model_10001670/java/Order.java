





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private String ReceipientName;
    private String ReceipientEmail;
    private String ReceipientContactNo;
    private String Order_ID;
    private String ReceipientAddress;
    private String GiftMessage;





    private Customer customer;




    private Payment payment;


    public Order(
        String ReceipientName,        String ReceipientEmail,        String ReceipientContactNo,        String Order_ID,        String ReceipientAddress,        String GiftMessage    ) {
        this.ReceipientName = ReceipientName;
        this.ReceipientEmail = ReceipientEmail;
        this.ReceipientContactNo = ReceipientContactNo;
        this.Order_ID = Order_ID;
        this.ReceipientAddress = ReceipientAddress;
        this.GiftMessage = GiftMessage;
    }


    public String getReceipientname() {
        return ReceipientName;
    }

    public void setReceipientname(String ReceipientName) {
        this.ReceipientName = ReceipientName;
    }
    public String getReceipientemail() {
        return ReceipientEmail;
    }

    public void setReceipientemail(String ReceipientEmail) {
        this.ReceipientEmail = ReceipientEmail;
    }
    public String getReceipientcontactno() {
        return ReceipientContactNo;
    }

    public void setReceipientcontactno(String ReceipientContactNo) {
        this.ReceipientContactNo = ReceipientContactNo;
    }
    public String getOrder_id() {
        return Order_ID;
    }

    public void setOrder_id(String Order_ID) {
        this.Order_ID = Order_ID;
    }
    public String getReceipientaddress() {
        return ReceipientAddress;
    }

    public void setReceipientaddress(String ReceipientAddress) {
        this.ReceipientAddress = ReceipientAddress;
    }
    public String getGiftmessage() {
        return GiftMessage;
    }

    public void setGiftmessage(String GiftMessage) {
        this.GiftMessage = GiftMessage;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }
    public Payment getPayment() {
        return payment;
    }

    public void setPayment(Payment payment) {
        this.payment = payment;
    }

}