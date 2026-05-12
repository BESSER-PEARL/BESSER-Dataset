





import java.util.List;
import java.util.ArrayList;

public class customer_Actor  {






    private cart_UseCase cart_usecase;




    private Order_Details_UseCase order_details_usecase;




    private Password_UseCase password_usecase;




    private Registration_UseCase registration_usecase;




    private Payment_UseCase payment_usecase;




    private Shipping_UseCase shipping_usecase;


    public customer_Actor(
    ) {
    }



    public cart_UseCase getCart_usecase() {
        return cart_usecase;
    }

    public void setCart_usecase(cart_UseCase cart_usecase) {
        this.cart_usecase = cart_usecase;
    }
    public Order_Details_UseCase getOrder_details_usecase() {
        return order_details_usecase;
    }

    public void setOrder_details_usecase(Order_Details_UseCase order_details_usecase) {
        this.order_details_usecase = order_details_usecase;
    }
    public Password_UseCase getPassword_usecase() {
        return password_usecase;
    }

    public void setPassword_usecase(Password_UseCase password_usecase) {
        this.password_usecase = password_usecase;
    }
    public Registration_UseCase getRegistration_usecase() {
        return registration_usecase;
    }

    public void setRegistration_usecase(Registration_UseCase registration_usecase) {
        this.registration_usecase = registration_usecase;
    }
    public Payment_UseCase getPayment_usecase() {
        return payment_usecase;
    }

    public void setPayment_usecase(Payment_UseCase payment_usecase) {
        this.payment_usecase = payment_usecase;
    }
    public Shipping_UseCase getShipping_usecase() {
        return shipping_usecase;
    }

    public void setShipping_usecase(Shipping_UseCase shipping_usecase) {
        this.shipping_usecase = shipping_usecase;
    }

}