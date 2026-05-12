





import java.util.List;
import java.util.ArrayList;

public class CarCallBox  {

    private String buttons;





    private Car car;


    public CarCallBox(
        String buttons    ) {
        this.buttons = buttons;
    }


    public String getButtons() {
        return buttons;
    }

    public void setButtons(String buttons) {
        this.buttons = buttons;
    }

    public Car getCar() {
        return car;
    }

    public void setCar(Car car) {
        this.car = car;
    }

}