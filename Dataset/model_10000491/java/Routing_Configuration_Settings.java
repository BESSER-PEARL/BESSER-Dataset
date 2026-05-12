





import java.util.List;
import java.util.ArrayList;

public class Routing_Configuration_Settings  {

    private String Name;
    private String Overflow_Assignee;



    public Routing_Configuration_Settings(
        String Name,        String Overflow_Assignee    ) {
        this.Name = Name;
        this.Overflow_Assignee = Overflow_Assignee;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getOverflow_assignee() {
        return Overflow_Assignee;
    }

    public void setOverflow_assignee(String Overflow_Assignee) {
        this.Overflow_Assignee = Overflow_Assignee;
    }


}