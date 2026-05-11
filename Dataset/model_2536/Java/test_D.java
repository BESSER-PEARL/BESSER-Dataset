





import java.util.List;
import java.util.ArrayList;

public class test_D  {

    private int yList;
    private String x;





    private test_C test_c;


    public test_D(
        int yList,        String x    ) {
        this.yList = yList;
        this.x = x;
    }


    public int getYlist() {
        return yList;
    }

    public void setYlist(int yList) {
        this.yList = yList;
    }
    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }

    public test_C getTest_c() {
        return test_c;
    }

    public void setTest_c(test_C test_c) {
        this.test_c = test_c;
    }

}