





import java.util.List;
import java.util.ArrayList;

public class ordersystem_Account  {

    private String accountNumber;
    private String paymentMethod;





    private ordersystem_Address ordersystem_address;




    private ordersystem_Address ordersystem_address;




    private ordersystem_Customer ordersystem_customer;




    private ordersystem_Customer ordersystem_customer;


    public ordersystem_Account(
        String accountNumber,        String paymentMethod    ) {
        this.accountNumber = accountNumber;
        this.paymentMethod = paymentMethod;
    }


    public String getAccountnumber() {
        return accountNumber;
    }

    public void setAccountnumber(String accountNumber) {
        this.accountNumber = accountNumber;
    }
    public String getPaymentmethod() {
        return paymentMethod;
    }

    public void setPaymentmethod(String paymentMethod) {
        this.paymentMethod = paymentMethod;
    }

    public ordersystem_Address getOrdersystem_address() {
        return ordersystem_address;
    }

    public void setOrdersystem_address(ordersystem_Address ordersystem_address) {
        this.ordersystem_address = ordersystem_address;
    }
    public ordersystem_Address getOrdersystem_address() {
        return ordersystem_address;
    }

    public void setOrdersystem_address(ordersystem_Address ordersystem_address) {
        this.ordersystem_address = ordersystem_address;
    }
    public ordersystem_Customer getOrdersystem_customer() {
        return ordersystem_customer;
    }

    public void setOrdersystem_customer(ordersystem_Customer ordersystem_customer) {
        this.ordersystem_customer = ordersystem_customer;
    }
    public ordersystem_Customer getOrdersystem_customer() {
        return ordersystem_customer;
    }

    public void setOrdersystem_customer(ordersystem_Customer ordersystem_customer) {
        this.ordersystem_customer = ordersystem_customer;
    }

}