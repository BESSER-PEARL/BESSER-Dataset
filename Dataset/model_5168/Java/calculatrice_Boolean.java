





import java.util.List;
import java.util.ArrayList;

public class calculatrice_Boolean extends BoolExpr {

    private String BoolValue;



    public calculatrice_Boolean(
        String BoolValue    ) {
        super(
        );
        this.BoolValue = BoolValue;
    }


    public String getBoolvalue() {
        return BoolValue;
    }

    public void setBoolvalue(String BoolValue) {
        this.BoolValue = BoolValue;
    }


}