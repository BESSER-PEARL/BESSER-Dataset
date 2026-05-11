





import java.util.List;
import java.util.ArrayList;

public class arduinoML_Brick extends NamedElement {

    private int pins;



    public arduinoML_Brick(
        int pins    ) {
        super(
        );
        this.pins = pins;
    }


    public int getPins() {
        return pins;
    }

    public void setPins(int pins) {
        this.pins = pins;
    }


}