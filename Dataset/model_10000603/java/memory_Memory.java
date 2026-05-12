





import java.util.List;
import java.util.ArrayList;

public class memory_Memory  {

    private None storage;





    private memory_MMU memory_mmu;


    public memory_Memory(
        None storage    ) {
        this.storage = storage;
    }


    public None getStorage() {
        return storage;
    }

    public void setStorage(None storage) {
        this.storage = storage;
    }

    public memory_MMU getMemory_mmu() {
        return memory_mmu;
    }

    public void setMemory_mmu(memory_MMU memory_mmu) {
        this.memory_mmu = memory_mmu;
    }

}