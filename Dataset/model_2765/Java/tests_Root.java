





import java.util.List;
import java.util.ArrayList;

public class tests_Root extends Named {






    private List<tests_TypeA> tests_typeas;




    private List<tests_TypeB> tests_typebs;


    public tests_Root(
    ) {
        super(
        );
        this.tests_typeas = new ArrayList<>();
        this.tests_typebs = new ArrayList<>();
    }

    public tests_Root(
        ArrayList<tests_TypeA> tests_typeas,        ArrayList<tests_TypeB> tests_typebs    ) {
        this.tests_typeas = tests_typeas;
        this.tests_typebs = tests_typebs;
    }


    public List<tests_TypeA> getTests_typeas() {
        return tests_typeas;
    }

    public void addTests_typea(Tests_typea tests_typea) {
        this.tests_typeas.add(tests_typea);
    }
    public List<tests_TypeB> getTests_typebs() {
        return tests_typebs;
    }

    public void addTests_typeb(Tests_typeb tests_typeb) {
        this.tests_typebs.add(tests_typeb);
    }

}