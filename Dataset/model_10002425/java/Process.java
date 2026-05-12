





import java.util.List;
import java.util.ArrayList;

public class Process  {

    private String registers;
    private String name;
    private None processState;
    private int memoryUseage;





    private Page page;


    public Process(
        String registers,        String name,        None processState,        int memoryUseage    ) {
        this.registers = registers;
        this.name = name;
        this.processState = processState;
        this.memoryUseage = memoryUseage;
    }


    public String getRegisters() {
        return registers;
    }

    public void setRegisters(String registers) {
        this.registers = registers;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public None getProcessstate() {
        return processState;
    }

    public void setProcessstate(None processState) {
        this.processState = processState;
    }
    public int getMemoryuseage() {
        return memoryUseage;
    }

    public void setMemoryuseage(int memoryUseage) {
        this.memoryUseage = memoryUseage;
    }

    public Page getPage() {
        return page;
    }

    public void setPage(Page page) {
        this.page = page;
    }

}