





import java.util.List;
import java.util.ArrayList;

public class Button  {

    private boolean IsOn;
    private String Clicked;
    private int FloorNumber;



    public Button(
        boolean IsOn,        String Clicked,        int FloorNumber    ) {
        this.IsOn = IsOn;
        this.Clicked = Clicked;
        this.FloorNumber = FloorNumber;
    }


    public boolean getIson() {
        return IsOn;
    }

    public void setIson(boolean IsOn) {
        this.IsOn = IsOn;
    }
    public String getClicked() {
        return Clicked;
    }

    public void setClicked(String Clicked) {
        this.Clicked = Clicked;
    }
    public int getFloornumber() {
        return FloorNumber;
    }

    public void setFloornumber(int FloorNumber) {
        this.FloorNumber = FloorNumber;
    }


}