





import java.util.List;
import java.util.ArrayList;

public class jpql_ExistsExpression extends Expression {

    private boolean isNot;





    private jpql_SelectStatement jpql_selectstatement;


    public jpql_ExistsExpression(
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

    public jpql_SelectStatement getJpql_selectstatement() {
        return jpql_selectstatement;
    }

    public void setJpql_selectstatement(jpql_SelectStatement jpql_selectstatement) {
        this.jpql_selectstatement = jpql_selectstatement;
    }

}