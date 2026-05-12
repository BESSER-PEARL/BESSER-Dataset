





import java.util.List;
import java.util.ArrayList;

public class Elevator_Button  {






    private List<Button> buttons;


    public Elevator_Button(
    ) {
        this.buttons = new ArrayList<>();
    }

    public Elevator_Button(
        ArrayList<Button> buttons    ) {
        this.buttons = buttons;
    }


    public List<Button> getButtons() {
        return buttons;
    }

    public void addButton(Button button) {
        this.buttons.add(button);
    }

}