





import java.util.List;
import java.util.ArrayList;

public class cpu_UnconditionalJumpExecutableInstruction  {

    private None cpu;
    private int address;



    public cpu_UnconditionalJumpExecutableInstruction(
        None cpu,        int address    ) {
        this.cpu = cpu;
        this.address = address;
    }


    public None getCpu() {
        return cpu;
    }

    public void setCpu(None cpu) {
        this.cpu = cpu;
    }
    public int getAddress() {
        return address;
    }

    public void setAddress(int address) {
        this.address = address;
    }


}