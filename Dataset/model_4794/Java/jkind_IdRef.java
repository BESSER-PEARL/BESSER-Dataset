





import java.util.List;
import java.util.ArrayList;

public class jkind_IdRef  {

    private String name;





    private jkind_IdExpr jkind_idexpr;


    public jkind_IdRef(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public jkind_IdExpr getJkind_idexpr() {
        return jkind_idexpr;
    }

    public void setJkind_idexpr(jkind_IdExpr jkind_idexpr) {
        this.jkind_idexpr = jkind_idexpr;
    }

}