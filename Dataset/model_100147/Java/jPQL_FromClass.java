





import java.util.List;
import java.util.ArrayList;

public class jPQL_FromClass extends FromEntry {






    private List<jPQL_FromJoin> jpql_fromjoins;


    public jPQL_FromClass(
    ) {
        super(
        );
        this.jpql_fromjoins = new ArrayList<>();
    }

    public jPQL_FromClass(
        ArrayList<jPQL_FromJoin> jpql_fromjoins    ) {
        this.jpql_fromjoins = jpql_fromjoins;
    }


    public List<jPQL_FromJoin> getJpql_fromjoins() {
        return jpql_fromjoins;
    }

    public void addJpql_fromjoin(Jpql_fromjoin jpql_fromjoin) {
        this.jpql_fromjoins.add(jpql_fromjoin);
    }

}