





import java.util.List;
import java.util.ArrayList;

public class MyClass3  {

    private String attribute;





    private MyClass myclass;




    private MyClass2 myclass2;


    public MyClass3(
        String attribute    ) {
        this.attribute = attribute;
    }


    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }

    public MyClass getMyclass() {
        return myclass;
    }

    public void setMyclass(MyClass myclass) {
        this.myclass = myclass;
    }
    public MyClass2 getMyclass2() {
        return myclass2;
    }

    public void setMyclass2(MyClass2 myclass2) {
        this.myclass2 = myclass2;
    }

}