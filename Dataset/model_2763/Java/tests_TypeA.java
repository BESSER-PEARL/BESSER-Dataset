





import java.util.List;
import java.util.ArrayList;

public class tests_TypeA extends Named {






    private tests_TypeB tests_typeb;




    private List<tests_TypeB> tests_typebs;


    public tests_TypeA(
    ) {
        super(
        );
        this.tests_typebs = new ArrayList<>();
    }

    public tests_TypeA(
        ArrayList<tests_TypeB> tests_typebs    ) {
        this.tests_typebs = tests_typebs;
    }


    public tests_TypeB getTests_typeb() {
        return tests_typeb;
    }

    public void setTests_typeb(tests_TypeB tests_typeb) {
        this.tests_typeb = tests_typeb;
    }
    public List<tests_TypeB> getTests_typebs() {
        return tests_typebs;
    }

    public void addTests_typeb(Tests_typeb tests_typeb) {
        this.tests_typebs.add(tests_typeb);
    }

}