





import java.util.List;
import java.util.ArrayList;

public class introduction_Y  {

    private int test;
    private String id;





    private introduction_A introduction_a;


    public introduction_Y(
        int test,        String id    ) {
        this.test = test;
        this.id = id;
    }


    public int getTest() {
        return test;
    }

    public void setTest(int test) {
        this.test = test;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public introduction_A getIntroduction_a() {
        return introduction_a;
    }

    public void setIntroduction_a(introduction_A introduction_a) {
        this.introduction_a = introduction_a;
    }

}