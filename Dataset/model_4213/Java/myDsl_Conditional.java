





import java.util.List;
import java.util.ArrayList;

public class myDsl_Conditional extends Expression {

    private String name;
    private int value3;
    private int value2;



    public myDsl_Conditional(
        String name,        int value3,        int value2    ) {
        super(
        );
        this.name = name;
        this.value3 = value3;
        this.value2 = value2;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getValue3() {
        return value3;
    }

    public void setValue3(int value3) {
        this.value3 = value3;
    }
    public int getValue2() {
        return value2;
    }

    public void setValue2(int value2) {
        this.value2 = value2;
    }


}