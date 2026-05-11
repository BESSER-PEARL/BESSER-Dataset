





import java.util.List;
import java.util.ArrayList;

public class grammar_features_ClassWithAttributes extends Child {

    private String a1;
    private boolean a2;



    public grammar_features_ClassWithAttributes(
        String a1,        boolean a2    ) {
        super(
        );
        this.a1 = a1;
        this.a2 = a2;
    }


    public String getA1() {
        return a1;
    }

    public void setA1(String a1) {
        this.a1 = a1;
    }
    public boolean getA2() {
        return a2;
    }

    public void setA2(boolean a2) {
        this.a2 = a2;
    }


}