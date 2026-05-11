





import java.util.List;
import java.util.ArrayList;

public class mytest_A extends EModelElement {

    private String name;





    private mytest_MyRoot mytest_myroot;


    public mytest_A(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public mytest_MyRoot getMytest_myroot() {
        return mytest_myroot;
    }

    public void setMytest_myroot(mytest_MyRoot mytest_myroot) {
        this.mytest_myroot = mytest_myroot;
    }

}