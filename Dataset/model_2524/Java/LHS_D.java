





import java.util.List;
import java.util.ArrayList;

public class LHS_D  {

    private String name;





    private LHS_B lhs_b;


    public LHS_D(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public LHS_B getLhs_b() {
        return lhs_b;
    }

    public void setLhs_b(LHS_B lhs_b) {
        this.lhs_b = lhs_b;
    }

}