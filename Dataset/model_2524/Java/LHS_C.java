





import java.util.List;
import java.util.ArrayList;

public class LHS_C  {

    private String name;





    private LHS_A lhs_a;


    public LHS_C(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public LHS_A getLhs_a() {
        return lhs_a;
    }

    public void setLhs_a(LHS_A lhs_a) {
        this.lhs_a = lhs_a;
    }

}