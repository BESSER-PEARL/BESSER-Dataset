





import java.util.List;
import java.util.ArrayList;

public class shr5_Credstick extends AbstraktGegenstand {

    private String currentValue;
    private int maxValue;



    public shr5_Credstick(
        String currentValue,        int maxValue    ) {
        super(
        );
        this.currentValue = currentValue;
        this.maxValue = maxValue;
    }


    public String getCurrentvalue() {
        return currentValue;
    }

    public void setCurrentvalue(String currentValue) {
        this.currentValue = currentValue;
    }
    public int getMaxvalue() {
        return maxValue;
    }

    public void setMaxvalue(int maxValue) {
        this.maxValue = maxValue;
    }


}