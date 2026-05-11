





import java.util.List;
import java.util.ArrayList;

public class xunit_Action  {

    private String desc;





    private xunit_Assertion xunit_assertion;


    public xunit_Action(
        String desc    ) {
        this.desc = desc;
    }


    public String getDesc() {
        return desc;
    }

    public void setDesc(String desc) {
        this.desc = desc;
    }

    public xunit_Assertion getXunit_assertion() {
        return xunit_assertion;
    }

    public void setXunit_assertion(xunit_Assertion xunit_assertion) {
        this.xunit_assertion = xunit_assertion;
    }

}