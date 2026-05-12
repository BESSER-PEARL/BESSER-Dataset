





import java.util.List;
import java.util.ArrayList;

public class jpql_InQueryExpression extends InExpression {






    private jpql_SelectStatement jpql_selectstatement;


    public jpql_InQueryExpression(
    ) {
        super(
        );
    }



    public jpql_SelectStatement getJpql_selectstatement() {
        return jpql_selectstatement;
    }

    public void setJpql_selectstatement(jpql_SelectStatement jpql_selectstatement) {
        this.jpql_selectstatement = jpql_selectstatement;
    }

}