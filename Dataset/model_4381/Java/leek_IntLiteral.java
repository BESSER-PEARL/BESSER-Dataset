





import java.util.List;
import java.util.ArrayList;

public class leek_IntLiteral extends Expression {

    private int value;



    public leek_IntLiteral(
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