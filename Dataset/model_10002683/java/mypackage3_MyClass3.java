





import java.util.List;
import java.util.ArrayList;

public class mypackage3_MyClass3  {

    private String attribute3_1;





    private List<mypackage2_MyClass2> mypackage2_myclass2s;


    public mypackage3_MyClass3(
        String attribute3_1    ) {
        this.attribute3_1 = attribute3_1;
        this.mypackage2_myclass2s = new ArrayList<>();
    }

    public mypackage3_MyClass3(
        String attribute3_1        ArrayList<mypackage2_MyClass2> mypackage2_myclass2s    ) {
        this.attribute3_1 = attribute3_1;
        this.mypackage2_myclass2s = mypackage2_myclass2s;
    }

    public String getAttribute3_1() {
        return attribute3_1;
    }

    public void setAttribute3_1(String attribute3_1) {
        this.attribute3_1 = attribute3_1;
    }

    public List<mypackage2_MyClass2> getMypackage2_myclass2s() {
        return mypackage2_myclass2s;
    }

    public void addMypackage2_myclass2(Mypackage2_myclass2 mypackage2_myclass2) {
        this.mypackage2_myclass2s.add(mypackage2_myclass2);
    }

}