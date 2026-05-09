





import java.util.List;
import java.util.ArrayList;

public class Classes_Interactionlayer_LoginController  {






    private PaymentHandler paymenthandler;




    private UserHandler userhandler;




    private GUIController guicontroller;


    public Classes_Interactionlayer_LoginController(
    ) {
    }



    public PaymentHandler getPaymenthandler() {
        return paymenthandler;
    }

    public void setPaymenthandler(PaymentHandler paymenthandler) {
        this.paymenthandler = paymenthandler;
    }
    public UserHandler getUserhandler() {
        return userhandler;
    }

    public void setUserhandler(UserHandler userhandler) {
        this.userhandler = userhandler;
    }
    public GUIController getGuicontroller() {
        return guicontroller;
    }

    public void setGuicontroller(GUIController guicontroller) {
        this.guicontroller = guicontroller;
    }

}