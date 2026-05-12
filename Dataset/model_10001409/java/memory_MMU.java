





import java.util.List;
import java.util.ArrayList;

public class memory_MMU  {

    private None RAM;





    private memory_Memory memory_memory;


    public memory_MMU(
        None RAM    ) {
        this.RAM = RAM;
    }


    public None getRam() {
        return RAM;
    }

    public void setRam(None RAM) {
        this.RAM = RAM;
    }

    public memory_Memory getMemory_memory() {
        return memory_memory;
    }

    public void setMemory_memory(memory_Memory memory_memory) {
        this.memory_memory = memory_memory;
    }

}