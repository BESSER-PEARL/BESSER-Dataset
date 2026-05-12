





import java.util.List;
import java.util.ArrayList;

public class BaseBO  {

    private int newInt;
    private boolean newBool;
    private String testString;



    public BaseBO(
        int newInt,        boolean newBool,        String testString    ) {
        this.newInt = newInt;
        this.newBool = newBool;
        this.testString = testString;
    }


    public int getNewint() {
        return newInt;
    }

    public void setNewint(int newInt) {
        this.newInt = newInt;
    }
    public boolean getNewbool() {
        return newBool;
    }

    public void setNewbool(boolean newBool) {
        this.newBool = newBool;
    }
    public String getTeststring() {
        return testString;
    }

    public void setTeststring(String testString) {
        this.testString = testString;
    }


}