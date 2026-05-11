





import java.util.List;
import java.util.ArrayList;

public class tests_TypeB extends Named {






    private tests_TypeA tests_typea;




    private List<tests_TypeA> tests_typeas;


    public tests_TypeB(
    ) {
        super(
        );
        this.tests_typeas = new ArrayList<>();
    }

    public tests_TypeB(
        ArrayList<tests_TypeA> tests_typeas    ) {
        this.tests_typeas = tests_typeas;
    }


    public tests_TypeA getTests_typea() {
        return tests_typea;
    }

    public void setTests_typea(tests_TypeA tests_typea) {
        this.tests_typea = tests_typea;
    }
    public List<tests_TypeA> getTests_typeas() {
        return tests_typeas;
    }

    public void addTests_typea(Tests_typea tests_typea) {
        this.tests_typeas.add(tests_typea);
    }

}