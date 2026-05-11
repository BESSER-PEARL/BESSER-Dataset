





import java.util.List;
import java.util.ArrayList;

public class mytest_MyRoot  {






    private List<mytest_A> mytest_as;




    private List<mytest_B> mytest_bs;




    private List<mytest_B> mytest_bs;


    public mytest_MyRoot(
    ) {
        this.mytest_as = new ArrayList<>();
        this.mytest_bs = new ArrayList<>();
        this.mytest_bs = new ArrayList<>();
    }

    public mytest_MyRoot(
        ArrayList<mytest_A> mytest_as,        ArrayList<mytest_B> mytest_bs,        ArrayList<mytest_B> mytest_bs    ) {
        this.mytest_as = mytest_as;
        this.mytest_bs = mytest_bs;
        this.mytest_bs = mytest_bs;
    }


    public List<mytest_A> getMytest_as() {
        return mytest_as;
    }

    public void addMytest_a(Mytest_a mytest_a) {
        this.mytest_as.add(mytest_a);
    }
    public List<mytest_B> getMytest_bs() {
        return mytest_bs;
    }

    public void addMytest_b(Mytest_b mytest_b) {
        this.mytest_bs.add(mytest_b);
    }
    public List<mytest_B> getMytest_bs() {
        return mytest_bs;
    }

    public void addMytest_b(Mytest_b mytest_b) {
        this.mytest_bs.add(mytest_b);
    }

}