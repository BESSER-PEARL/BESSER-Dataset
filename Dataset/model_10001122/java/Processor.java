





import java.util.List;
import java.util.ArrayList;

public class Processor  {






    private List<Memory_Interface> memory_interfaces;


    public Processor(
    ) {
        this.memory_interfaces = new ArrayList<>();
    }

    public Processor(
        ArrayList<Memory_Interface> memory_interfaces    ) {
        this.memory_interfaces = memory_interfaces;
    }


    public List<Memory_Interface> getMemory_interfaces() {
        return memory_interfaces;
    }

    public void addMemory_interface(Memory_interface memory_interface) {
        this.memory_interfaces.add(memory_interface);
    }

}