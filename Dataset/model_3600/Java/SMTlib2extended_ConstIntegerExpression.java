





import java.util.List;
import java.util.ArrayList;

public class SMTlib2extended_ConstIntegerExpression extends ConstExpression {

    private int width;
    private int value;



    public SMTlib2extended_ConstIntegerExpression(
        int width,        int value    ) {
        super(
        );
        this.width = width;
        this.value = value;
    }


    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }
    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }


}