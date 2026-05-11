





import java.util.List;
import java.util.ArrayList;

public class simpletest_X  {






    private List<simpletest_A> simpletest_as;


    public simpletest_X(
    ) {
        this.simpletest_as = new ArrayList<>();
    }

    public simpletest_X(
        ArrayList<simpletest_A> simpletest_as    ) {
        this.simpletest_as = simpletest_as;
    }


    public List<simpletest_A> getSimpletest_as() {
        return simpletest_as;
    }

    public void addSimpletest_a(Simpletest_a simpletest_a) {
        this.simpletest_as.add(simpletest_a);
    }

}