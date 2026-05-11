





import java.util.List;
import java.util.ArrayList;

public class RHS_V  {

    private String name;





    private RHS_X rhs_x;


    public RHS_V(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public RHS_X getRhs_x() {
        return rhs_x;
    }

    public void setRhs_x(RHS_X rhs_x) {
        this.rhs_x = rhs_x;
    }

}