





import java.util.List;
import java.util.ArrayList;

public class memory_Word  {

    private int data;





    private List<memory_Memory> memory_memorys;


    public memory_Word(
        int data    ) {
        this.data = data;
        this.memory_memorys = new ArrayList<>();
    }

    public memory_Word(
        int data        ArrayList<memory_Memory> memory_memorys    ) {
        this.data = data;
        this.memory_memorys = memory_memorys;
    }

    public int getData() {
        return data;
    }

    public void setData(int data) {
        this.data = data;
    }

    public List<memory_Memory> getMemory_memorys() {
        return memory_memorys;
    }

    public void addMemory_memory(Memory_memory memory_memory) {
        this.memory_memorys.add(memory_memory);
    }

}