





import java.util.List;
import java.util.ArrayList;

public class MyClass2  {






    private List<MyClass> myclasss;


    public MyClass2(
    ) {
        this.myclasss = new ArrayList<>();
    }

    public MyClass2(
        ArrayList<MyClass> myclasss    ) {
        this.myclasss = myclasss;
    }


    public List<MyClass> getMyclasss() {
        return myclasss;
    }

    public void addMyclass(Myclass myclass) {
        this.myclasss.add(myclass);
    }

}