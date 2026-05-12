





import java.util.List;
import java.util.ArrayList;

public class cpu_ExecutableInstruction  {

    private None type;
    private None registers;



    public cpu_ExecutableInstruction(
        None type,        None registers    ) {
        this.type = type;
        this.registers = registers;
    }


    public None getType() {
        return type;
    }

    public void setType(None type) {
        this.type = type;
    }
    public None getRegisters() {
        return registers;
    }

    public void setRegisters(None registers) {
        this.registers = registers;
    }


}