





import java.util.List;
import java.util.ArrayList;

public class company_TestClass  {

    private int intAttribute2;
    private int intAttribute1;
    private String stringAttribute2;
    private String stringAttribute1;



    public company_TestClass(
        int intAttribute2,        int intAttribute1,        String stringAttribute2,        String stringAttribute1    ) {
        this.intAttribute2 = intAttribute2;
        this.intAttribute1 = intAttribute1;
        this.stringAttribute2 = stringAttribute2;
        this.stringAttribute1 = stringAttribute1;
    }


    public int getIntattribute2() {
        return intAttribute2;
    }

    public void setIntattribute2(int intAttribute2) {
        this.intAttribute2 = intAttribute2;
    }
    public int getIntattribute1() {
        return intAttribute1;
    }

    public void setIntattribute1(int intAttribute1) {
        this.intAttribute1 = intAttribute1;
    }
    public String getStringattribute2() {
        return stringAttribute2;
    }

    public void setStringattribute2(String stringAttribute2) {
        this.stringAttribute2 = stringAttribute2;
    }
    public String getStringattribute1() {
        return stringAttribute1;
    }

    public void setStringattribute1(String stringAttribute1) {
        this.stringAttribute1 = stringAttribute1;
    }


}