





import java.util.List;
import java.util.ArrayList;

public class avm_Workflow  {

    private String Name;





    private avm_TestBench avm_testbench;


    public avm_Workflow(
        String Name    ) {
        this.Name = Name;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public avm_TestBench getAvm_testbench() {
        return avm_testbench;
    }

    public void setAvm_testbench(avm_TestBench avm_testbench) {
        this.avm_testbench = avm_testbench;
    }

}