





import java.util.List;
import java.util.ArrayList;

public class kmLogo_CallStack  {






    private kmLogo_Turtle kmlogo_turtle;




    private List<kmLogo_StackFrame> kmlogo_stackframes;


    public kmLogo_CallStack(
    ) {
        this.kmlogo_stackframes = new ArrayList<>();
    }

    public kmLogo_CallStack(
        ArrayList<kmLogo_StackFrame> kmlogo_stackframes    ) {
        this.kmlogo_stackframes = kmlogo_stackframes;
    }


    public kmLogo_Turtle getKmlogo_turtle() {
        return kmlogo_turtle;
    }

    public void setKmlogo_turtle(kmLogo_Turtle kmlogo_turtle) {
        this.kmlogo_turtle = kmlogo_turtle;
    }
    public List<kmLogo_StackFrame> getKmlogo_stackframes() {
        return kmlogo_stackframes;
    }

    public void addKmlogo_stackframe(Kmlogo_stackframe kmlogo_stackframe) {
        this.kmlogo_stackframes.add(kmlogo_stackframe);
    }

}