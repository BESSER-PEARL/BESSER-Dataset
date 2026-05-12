





import java.util.List;
import java.util.ArrayList;

public class Process  {

    private String processState;
    private String registers;
    private int memoryUseage;
    private String name;



    public Process(
        String processState,        String registers,        int memoryUseage,        String name    ) {
        this.processState = processState;
        this.registers = registers;
        this.memoryUseage = memoryUseage;
        this.name = name;
    }


    public String getProcessstate() {
        return processState;
    }

    public void setProcessstate(String processState) {
        this.processState = processState;
    }
    public String getRegisters() {
        return registers;
    }

    public void setRegisters(String registers) {
        this.registers = registers;
    }
    public int getMemoryuseage() {
        return memoryUseage;
    }

    public void setMemoryuseage(int memoryUseage) {
        this.memoryUseage = memoryUseage;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}