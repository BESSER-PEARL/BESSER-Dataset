





import java.util.List;
import java.util.ArrayList;

public class CPU  {

    private String registers;





    private Operating_System operating_system;


    public CPU(
        String registers    ) {
        this.registers = registers;
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