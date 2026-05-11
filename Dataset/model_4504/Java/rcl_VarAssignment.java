





import java.util.List;
import java.util.ArrayList;

public class rcl_VarAssignment extends Statement {

    private boolean name;



    public rcl_VarAssignment(
        boolean name    ) {
        super(
        );
        this.name = name;
    }


    public boolean getName() {
        return name;
    }

    public void setName(boolean name) {
        this.name = name;
    }


}