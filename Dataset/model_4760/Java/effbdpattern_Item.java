





import java.util.List;
import java.util.ArrayList;

public class effbdpattern_Item  {

    private String name;





    private effbdpattern_Flow effbdpattern_flow;


    public effbdpattern_Item(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public effbdpattern_Flow getEffbdpattern_flow() {
        return effbdpattern_flow;
    }

    public void setEffbdpattern_flow(effbdpattern_Flow effbdpattern_flow) {
        this.effbdpattern_flow = effbdpattern_flow;
    }

}