





import java.util.List;
import java.util.ArrayList;

public class Remote_Controller_Interface  {

    private String Control_Garade_Door;
    private String Bluebooth;



    public Remote_Controller_Interface(
        String Control_Garade_Door,        String Bluebooth    ) {
        this.Control_Garade_Door = Control_Garade_Door;
        this.Bluebooth = Bluebooth;
    }


    public String getControl_garade_door() {
        return Control_Garade_Door;
    }

    public void setControl_garade_door(String Control_Garade_Door) {
        this.Control_Garade_Door = Control_Garade_Door;
    }
    public String getBluebooth() {
        return Bluebooth;
    }

    public void setBluebooth(String Bluebooth) {
        this.Bluebooth = Bluebooth;
    }


}