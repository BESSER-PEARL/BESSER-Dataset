





import java.util.List;
import java.util.ArrayList;

public class test_A  {






    private test_Compo test_compo;




    private List<test_B> test_bs;


    public test_A(
    ) {
        this.test_bs = new ArrayList<>();
    }

    public test_A(
        ArrayList<test_B> test_bs    ) {
        this.test_bs = test_bs;
    }


    public test_Compo getTest_compo() {
        return test_compo;
    }

    public void setTest_compo(test_Compo test_compo) {
        this.test_compo = test_compo;
    }
    public List<test_B> getTest_bs() {
        return test_bs;
    }

    public void addTest_b(Test_b test_b) {
        this.test_bs.add(test_b);
    }

}