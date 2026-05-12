





import java.util.List;
import java.util.ArrayList;

public class cpu_DMAChannel  {

    private String mmu;





    private cpu_CPU cpu_cpu;


    public cpu_DMAChannel(
        String mmu    ) {
        this.mmu = mmu;
    }


    public String getMmu() {
        return mmu;
    }

    public void setMmu(String mmu) {
        this.mmu = mmu;
    }

    public cpu_CPU getCpu_cpu() {
        return cpu_cpu;
    }

    public void setCpu_cpu(cpu_CPU cpu_cpu) {
        this.cpu_cpu = cpu_cpu;
    }

}