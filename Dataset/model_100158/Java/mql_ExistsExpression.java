





import java.util.List;
import java.util.ArrayList;

public class mql_ExistsExpression extends Expression {

    private boolean isNot;





    private mql_SelectStatement mql_selectstatement;


    public mql_ExistsExpression(
        boolean isNot    ) {
        super(
        );
        this.isNot = isNot;
    }


    public boolean getIsnot() {
        return isNot;
    }

    public void setIsnot(boolean isNot) {
        this.isNot = isNot;
    }

    public mql_SelectStatement getMql_selectstatement() {
        return mql_selectstatement;
    }

    public void setMql_selectstatement(mql_SelectStatement mql_selectstatement) {
        this.mql_selectstatement = mql_selectstatement;
    }

}