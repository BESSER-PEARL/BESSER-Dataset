





import java.util.List;
import java.util.ArrayList;

public class ORDB4ORA_Check extends Restriction {

    private String Name;
    private String Condition;



    public ORDB4ORA_Check(
        String Name,        String Condition    ) {
        super(
        );
        this.Name = Name;
        this.Condition = Condition;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getCondition() {
        return Condition;
    }

    public void setCondition(String Condition) {
        this.Condition = Condition;
    }


}