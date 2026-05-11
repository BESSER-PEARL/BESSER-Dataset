





import java.util.List;
import java.util.ArrayList;

public class dSL_TouchLiteral extends Expression {

    private String touch;



    public dSL_TouchLiteral(
        String touch    ) {
        super(
        );
        this.touch = touch;
    }


    public String getTouch() {
        return touch;
    }

    public void setTouch(String touch) {
        this.touch = touch;
    }


}