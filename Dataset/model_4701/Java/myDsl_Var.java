





import java.util.List;
import java.util.ArrayList;

public class myDsl_Var extends TopLevelCmd, Expr {

    private String name;



    public myDsl_Var(
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