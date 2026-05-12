





import java.util.List;
import java.util.ArrayList;

public class Payment  {

    private int OrderID;
    private int PaymentID;
    private String Method;





    private Order order;


    public Payment(
        int OrderID,        int PaymentID,        String Method    ) {
        this.OrderID = OrderID;
        this.PaymentID = PaymentID;
        this.Method = Method;
    }


    public int getOrderid() {
        return OrderID;
    }

    public void setOrderid(int OrderID) {
        this.OrderID = OrderID;
    }
    public int getPaymentid() {
        return PaymentID;
    }

    public void setPaymentid(int PaymentID) {
        this.PaymentID = PaymentID;
    }
    public String getMethod() {
        return Method;
    }

    public void setMethod(String Method) {
        this.Method = Method;
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}