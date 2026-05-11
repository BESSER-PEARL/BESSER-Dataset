





import java.util.List;
import java.util.ArrayList;

public class anytype_TestAny  {

    private String name;
    private String any;
    private String myAny;
    private String a;



    public anytype_TestAny(
        String name,        String any,        String myAny,        String a    ) {
        this.name = name;
        this.any = any;
        this.myAny = myAny;
        this.a = a;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAny() {
        return any;
    }

    public void setAny(String any) {
        this.any = any;
    }
    public String getMyany() {
        return myAny;
    }

    public void setMyany(String myAny) {
        this.myAny = myAny;
    }
    public String getA() {
        return a;
    }

    public void setA(String a) {
        this.a = a;
    }


}