





import java.util.List;
import java.util.ArrayList;

public class ecdarText_ETForallExpression extends ETExpression {

    private String name;





    private ecdarText_ETType ecdartext_ettype;




    private ecdarText_ETExpression ecdartext_etexpression;


    public ecdarText_ETForallExpression(
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

    public ecdarText_ETType getEcdartext_ettype() {
        return ecdartext_ettype;
    }

    public void setEcdartext_ettype(ecdarText_ETType ecdartext_ettype) {
        this.ecdartext_ettype = ecdartext_ettype;
    }
    public ecdarText_ETExpression getEcdartext_etexpression() {
        return ecdartext_etexpression;
    }

    public void setEcdartext_etexpression(ecdarText_ETExpression ecdartext_etexpression) {
        this.ecdartext_etexpression = ecdartext_etexpression;
    }

}