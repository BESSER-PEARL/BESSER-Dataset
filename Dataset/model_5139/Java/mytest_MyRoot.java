





import java.util.List;
import java.util.ArrayList;

public class mytest_MyRoot  {






    private List<mytest_B> mytest_bs;


    public mytest_MyRoot(
    ) {
        this.mytest_bs = new ArrayList<>();
    }

    public mytest_MyRoot(
        ArrayList<mytest_B> mytest_bs    ) {
        this.mytest_bs = mytest_bs;
    }


    public List<mytest_B> getMytest_bs() {
        return mytest_bs;
    }

    public void addMytest_b(Mytest_b mytest_b) {
        this.mytest_bs.add(mytest_b);
    }

}