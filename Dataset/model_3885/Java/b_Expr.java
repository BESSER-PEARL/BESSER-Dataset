





import java.util.List;
import java.util.ArrayList;

public class b_Expr  {






    private b_If b_if;




    private b_IfCond b_ifcond;




    private b_Pre b_pre;


    public b_Expr(
    ) {
    }



    public b_If getB_if() {
        return b_if;
    }

    public void setB_if(b_If b_if) {
        this.b_if = b_if;
    }
    public b_IfCond getB_ifcond() {
        return b_ifcond;
    }

    public void setB_ifcond(b_IfCond b_ifcond) {
        this.b_ifcond = b_ifcond;
    }
    public b_Pre getB_pre() {
        return b_pre;
    }

    public void setB_pre(b_Pre b_pre) {
        this.b_pre = b_pre;
    }

}