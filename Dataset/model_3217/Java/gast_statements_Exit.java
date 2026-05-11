





import java.util.List;
import java.util.ArrayList;

public class gast_statements_Exit extends FlowInstr {

    private String name;



    public gast_statements_Exit(
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