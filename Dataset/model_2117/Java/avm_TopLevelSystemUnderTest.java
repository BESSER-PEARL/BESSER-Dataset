





import java.util.List;
import java.util.ArrayList;

public class avm_TopLevelSystemUnderTest extends ContainerInstanceBase {

    private String DesignID;





    private avm_TestBench avm_testbench;


    public avm_TopLevelSystemUnderTest(
        String DesignID    ) {
        super(
        );
        this.DesignID = DesignID;
    }


    public String getDesignid() {
        return DesignID;
    }

    public void setDesignid(String DesignID) {
        this.DesignID = DesignID;
    }

    public avm_TestBench getAvm_testbench() {
        return avm_testbench;
    }

    public void setAvm_testbench(avm_TestBench avm_testbench) {
        this.avm_testbench = avm_testbench;
    }

}