





import java.util.List;
import java.util.ArrayList;

public class ORDB4ORA_Check extends Restriction {

    private String Condition;



    public ORDB4ORA_Check(
        String Condition    ) {
        super(
        );
        this.Condition = Condition;
    }


    public String getCondition() {
        return Condition;
    }

    public void setCondition(String Condition) {
        this.Condition = Condition;
    }


}