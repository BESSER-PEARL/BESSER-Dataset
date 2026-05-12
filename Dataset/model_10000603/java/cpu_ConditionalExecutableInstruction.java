





import java.util.List;
import java.util.ArrayList;

public class cpu_ConditionalExecutableInstruction  {

    private int data;
    private None cache;
    private None cpu;
    private int dReg;
    private int bReg;



    public cpu_ConditionalExecutableInstruction(
        int data,        None cache,        None cpu,        int dReg,        int bReg    ) {
        this.data = data;
        this.cache = cache;
        this.cpu = cpu;
        this.dReg = dReg;
        this.bReg = bReg;
    }


    public int getData() {
        return data;
    }

    public void setData(int data) {
        this.data = data;
    }
    public None getCache() {
        return cache;
    }

    public void setCache(None cache) {
        this.cache = cache;
    }
    public None getCpu() {
        return cpu;
    }

    public void setCpu(None cpu) {
        this.cpu = cpu;
    }
    public int getDreg() {
        return dReg;
    }

    public void setDreg(int dReg) {
        this.dReg = dReg;
    }
    public int getBreg() {
        return bReg;
    }

    public void setBreg(int bReg) {
        this.bReg = bReg;
    }


}