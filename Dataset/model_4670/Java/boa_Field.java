





import java.util.List;
import java.util.ArrayList;

public class boa_Field  {

    private String name;





    private boa_Expr boa_expr;




    private boa_BObject boa_bobject;


    public boa_Field(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public boa_Expr getBoa_expr() {
        return boa_expr;
    }

    public void setBoa_expr(boa_Expr boa_expr) {
        this.boa_expr = boa_expr;
    }
    public boa_BObject getBoa_bobject() {
        return boa_bobject;
    }

    public void setBoa_bobject(boa_BObject boa_bobject) {
        this.boa_bobject = boa_bobject;
    }

}