





import java.util.List;
import java.util.ArrayList;

public class camel_requirement_VerticalScaleRequirement extends ScaleRequirement {

    private int minCores;
    private int minRAM;
    private int minStorage;
    private int maxStorage;
    private float maxCPU;
    private float minCPU;
    private int maxRAM;
    private int maxCores;





    private VM vm;


    public camel_requirement_VerticalScaleRequirement(
        int minCores,        int minRAM,        int minStorage,        int maxStorage,        float maxCPU,        float minCPU,        int maxRAM,        int maxCores    ) {
        super(
        );
        this.minCores = minCores;
        this.minRAM = minRAM;
        this.minStorage = minStorage;
        this.maxStorage = maxStorage;
        this.maxCPU = maxCPU;
        this.minCPU = minCPU;
        this.maxRAM = maxRAM;
        this.maxCores = maxCores;
    }


    public int getMincores() {
        return minCores;
    }

    public void setMincores(int minCores) {
        this.minCores = minCores;
    }
    public int getMinram() {
        return minRAM;
    }

    public void setMinram(int minRAM) {
        this.minRAM = minRAM;
    }
    public int getMinstorage() {
        return minStorage;
    }

    public void setMinstorage(int minStorage) {
        this.minStorage = minStorage;
    }
    public int getMaxstorage() {
        return maxStorage;
    }

    public void setMaxstorage(int maxStorage) {
        this.maxStorage = maxStorage;
    }
    public float getMaxcpu() {
        return maxCPU;
    }

    public void setMaxcpu(float maxCPU) {
        this.maxCPU = maxCPU;
    }
    public float getMincpu() {
        return minCPU;
    }

    public void setMincpu(float minCPU) {
        this.minCPU = minCPU;
    }
    public int getMaxram() {
        return maxRAM;
    }

    public void setMaxram(int maxRAM) {
        this.maxRAM = maxRAM;
    }
    public int getMaxcores() {
        return maxCores;
    }

    public void setMaxcores(int maxCores) {
        this.maxCores = maxCores;
    }

    public VM getVm() {
        return vm;
    }

    public void setVm(VM vm) {
        this.vm = vm;
    }

}