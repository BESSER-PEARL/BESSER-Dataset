





import java.util.List;
import java.util.ArrayList;

public class customerDsl_POBox extends Address {

    private int number;



    public customerDsl_POBox(
        int number    ) {
        super(
        );
        this.number = number;
    }


    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }


}