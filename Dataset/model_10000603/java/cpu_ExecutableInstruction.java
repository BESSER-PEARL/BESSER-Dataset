





import java.util.List;
import java.util.ArrayList;

public class cpu_ExecutableInstruction  {

    private None registers;
    private None type;



    public cpu_ExecutableInstruction(
        None registers,        None type    ) {
        this.registers = registers;
        this.type = type;
    }


    public None getRegisters() {
        return registers;
    }

    public void setRegisters(None registers) {
        this.registers = registers;
    }
    public None getType() {
        return type;
    }

    public void setType(None type) {
        this.type = type;
    }


}