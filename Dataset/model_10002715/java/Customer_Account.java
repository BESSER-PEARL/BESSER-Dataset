





import java.util.List;
import java.util.ArrayList;

public class Customer_Account  {

    private String Login__;
    private String account__;





    private GUI_Screen gui_screen;


    public Customer_Account(
        String Login__,        String account__    ) {
        this.Login__ = Login__;
        this.account__ = account__;
    }


    public String getLogin__() {
        return Login__;
    }

    public void setLogin__(String Login__) {
        this.Login__ = Login__;
    }
    public String getAccount__() {
        return account__;
    }

    public void setAccount__(String account__) {
        this.account__ = account__;
    }

    public GUI_Screen getGui_screen() {
        return gui_screen;
    }

    public void setGui_screen(GUI_Screen gui_screen) {
        this.gui_screen = gui_screen;
    }

}