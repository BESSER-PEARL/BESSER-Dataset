





import java.util.List;
import java.util.ArrayList;

public class myDsl_PlusPlus extends unary_expression {

    private String plus;



    public myDsl_PlusPlus(
        String plus    ) {
        super(
        );
        this.plus = plus;
    }


    public String getPlus() {
        return plus;
    }

    public void setPlus(String plus) {
        this.plus = plus;
    }


}