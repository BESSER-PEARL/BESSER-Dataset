





import java.util.List;
import java.util.ArrayList;

public class blorqueScript_BSNumberConstant extends BSExpression {

    private int value;



    public blorqueScript_BSNumberConstant(
        int value    ) {
        super(
        );
        this.value = value;
    }


    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }


}