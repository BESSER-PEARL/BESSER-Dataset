





import java.util.List;
import java.util.ArrayList;

public class iot_Arduino  {

    private int pins;
    private String model;





    private iot_Board iot_board;


    public iot_Arduino(
        int pins,        String model    ) {
        this.pins = pins;
        this.model = model;
    }


    public int getPins() {
        return pins;
    }

    public void setPins(int pins) {
        this.pins = pins;
    }
    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        this.model = model;
    }

    public iot_Board getIot_board() {
        return iot_board;
    }

    public void setIot_board(iot_Board iot_board) {
        this.iot_board = iot_board;
    }

}