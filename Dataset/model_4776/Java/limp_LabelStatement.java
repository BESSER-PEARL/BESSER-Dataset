





import java.util.List;
import java.util.ArrayList;

public class limp_LabelStatement extends Statement {

    private String name;



    public limp_LabelStatement(
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