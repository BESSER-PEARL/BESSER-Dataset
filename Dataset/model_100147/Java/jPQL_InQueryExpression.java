





import java.util.List;
import java.util.ArrayList;

public class jPQL_InQueryExpression extends InExpression {






    private jPQL_SelectStatement jpql_selectstatement;


    public jPQL_InQueryExpression(
    ) {
        super(
        );
    }



    public jPQL_SelectStatement getJpql_selectstatement() {
        return jpql_selectstatement;
    }

    public void setJpql_selectstatement(jPQL_SelectStatement jpql_selectstatement) {
        this.jpql_selectstatement = jpql_selectstatement;
    }

}