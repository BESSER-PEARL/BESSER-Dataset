





import java.util.List;
import java.util.ArrayList;

public class noop_BreakStatement extends Statement {

    private String name;



    public noop_BreakStatement(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}