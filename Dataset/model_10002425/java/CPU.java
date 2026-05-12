





import java.util.List;
import java.util.ArrayList;

public class CPU  {

    private None interruptQueue;
    private String registers;





    private Operating_System operating_system;


    public CPU(
        None interruptQueue,        String registers    ) {
        this.interruptQueue = interruptQueue;
        this.registers = registers;
    }


    public None getInterruptqueue() {
        return interruptQueue;
    }

    public void setInterruptqueue(None interruptQueue) {
        this.interruptQueue = interruptQueue;
    }
    public String getRegisters() {
        return registers;
    }

    public void setRegisters(String registers) {
        this.registers = registers;
    }

    public Operating_System getOperating_system() {
        return operating_system;
    }

    public void setOperating_system(Operating_System operating_system) {
        this.operating_system = operating_system;
    }

}