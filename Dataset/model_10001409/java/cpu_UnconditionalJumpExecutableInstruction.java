





import java.util.List;
import java.util.ArrayList;

public class cpu_UnconditionalJumpExecutableInstruction  {

    private int address;
    private None cpu;



    public cpu_UnconditionalJumpExecutableInstruction(
        int address,        None cpu    ) {
        this.address = address;
        this.cpu = cpu;
    }


    public int getAddress() {
        return address;
    }

    public void setAddress(int address) {
        this.address = address;
    }
    public None getCpu() {
        return cpu;
    }

    public void setCpu(None cpu) {
        this.cpu = cpu;
    }


}