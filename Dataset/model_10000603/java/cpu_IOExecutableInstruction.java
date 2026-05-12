





import java.util.List;
import java.util.ArrayList;

public class cpu_IOExecutableInstruction  {

    private int reg1;
    private int address;
    private int reg2;



    public cpu_IOExecutableInstruction(
        int reg1,        int address,        int reg2    ) {
        this.reg1 = reg1;
        this.address = address;
        this.reg2 = reg2;
    }


    public int getReg1() {
        return reg1;
    }

    public void setReg1(int reg1) {
        this.reg1 = reg1;
    }
    public int getAddress() {
        return address;
    }

    public void setAddress(int address) {
        this.address = address;
    }
    public int getReg2() {
        return reg2;
    }

    public void setReg2(int reg2) {
        this.reg2 = reg2;
    }


}