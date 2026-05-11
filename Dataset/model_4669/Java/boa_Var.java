





import java.util.List;
import java.util.ArrayList;

public class boa_Var extends Expr {

    private String name;



    public boa_Var(
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