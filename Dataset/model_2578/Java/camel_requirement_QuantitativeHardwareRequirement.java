





import java.util.List;
import java.util.ArrayList;

public class camel_requirement_QuantitativeHardwareRequirement extends HardwareRequirement {

    private int minCores;
    private int minStorage;
    private int minRAM;
    private float maxCPU;
    private float minCPU;
    private int maxStorage;
    private int maxRAM;
    private int maxCores;



    public camel_requirement_QuantitativeHardwareRequirement(
        int minCores,        int minStorage,        int minRAM,        float maxCPU,        float minCPU,        int maxStorage,        int maxRAM,        int maxCores    ) {
        super(
        );
        this.minCores = minCores;
        this.minStorage = minStorage;
        this.minRAM = minRAM;
        this.maxCPU = maxCPU;
        this.minCPU = minCPU;
        this.maxStorage = maxStorage;
        this.maxRAM = maxRAM;
        this.maxCores = maxCores;
    }


    public int getMincores() {
        return minCores;
    }

    public void setMincores(int minCores) {
        this.minCores = minCores;
    }
    public int getMinstorage() {
        return minStorage;
    }

    public void setMinstorage(int minStorage) {
        this.minStorage = minStorage;
    }
    public int getMinram() {
        return minRAM;
    }

    public void setMinram(int minRAM) {
        this.minRAM = minRAM;
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
    public int getMaxstorage() {
        return maxStorage;
    }

    public void setMaxstorage(int maxStorage) {
        this.maxStorage = maxStorage;
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


}