





import java.util.List;
import java.util.ArrayList;

public class ORDB4ORA_Check extends Restriction {

    private String Condition;
    private String Name;



    public ORDB4ORA_Check(
        String Condition,        String Name    ) {
        super(
        );
        this.Condition = Condition;
        this.Name = Name;
    }


    public String getCondition() {
        return Condition;
    }

    public void setCondition(String Condition) {
        this.Condition = Condition;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }


}