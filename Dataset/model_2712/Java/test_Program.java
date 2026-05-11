





import java.util.List;
import java.util.ArrayList;

public class test_Program  {






    private List<test_A> test_as;




    private List<test_C> test_cs;


    public test_Program(
    ) {
        this.test_as = new ArrayList<>();
        this.test_cs = new ArrayList<>();
    }

    public test_Program(
        ArrayList<test_A> test_as,        ArrayList<test_C> test_cs    ) {
        this.test_as = test_as;
        this.test_cs = test_cs;
    }


    public List<test_A> getTest_as() {
        return test_as;
    }

    public void addTest_a(Test_a test_a) {
        this.test_as.add(test_a);
    }
    public List<test_C> getTest_cs() {
        return test_cs;
    }

    public void addTest_c(Test_c test_c) {
        this.test_cs.add(test_c);
    }

}