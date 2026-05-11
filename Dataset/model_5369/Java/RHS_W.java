





import java.util.List;
import java.util.ArrayList;

public class RHS_W  {

    private String name;





    private RHS_Y rhs_y;


    public RHS_W(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public RHS_Y getRhs_y() {
        return rhs_y;
    }

    public void setRhs_y(RHS_Y rhs_y) {
        this.rhs_y = rhs_y;
    }

}