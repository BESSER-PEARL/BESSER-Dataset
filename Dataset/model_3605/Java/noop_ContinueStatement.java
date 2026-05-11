





import java.util.List;
import java.util.ArrayList;

public class noop_ContinueStatement extends Statement {

    private String name;



    public noop_ContinueStatement(
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