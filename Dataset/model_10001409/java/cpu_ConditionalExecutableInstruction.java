





import java.util.List;
import java.util.ArrayList;

public class cpu_ConditionalExecutableInstruction  {

    private None cpu;
    private int data;
    private None cache;
    private int dReg;
    private int bReg;



    public cpu_ConditionalExecutableInstruction(
        None cpu,        int data,        None cache,        int dReg,        int bReg    ) {
        this.cpu = cpu;
        this.data = data;
        this.cache = cache;
        this.dReg = dReg;
        this.bReg = bReg;
    }


    public None getCpu() {
        return cpu;
    }

    public void setCpu(None cpu) {
        this.cpu = cpu;
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