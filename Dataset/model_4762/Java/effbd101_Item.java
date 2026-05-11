





import java.util.List;
import java.util.ArrayList;

public class effbd101_Item  {

    private String name;





    private effbd101_Flow effbd101_flow;


    public effbd101_Item(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public effbd101_Flow getEffbd101_flow() {
        return effbd101_flow;
    }

    public void setEffbd101_flow(effbd101_Flow effbd101_flow) {
        this.effbd101_flow = effbd101_flow;
    }

}