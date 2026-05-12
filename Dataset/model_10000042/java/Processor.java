





import java.util.List;
import java.util.ArrayList;

public class Processor  {






    private List<Program> programs;




    private List<Memory_Interface> memory_interfaces;




    private List<Machine> machines;


    public Processor(
    ) {
        this.programs = new ArrayList<>();
        this.memory_interfaces = new ArrayList<>();
        this.machines = new ArrayList<>();
    }

    public Processor(
        ArrayList<Program> programs,        ArrayList<Memory_Interface> memory_interfaces,        ArrayList<Machine> machines    ) {
        this.programs = programs;
        this.memory_interfaces = memory_interfaces;
        this.machines = machines;
    }


    public List<Program> getPrograms() {
        return programs;
    }

    public void addProgram(Program program) {
        this.programs.add(program);
    }
    public List<Memory_Interface> getMemory_interfaces() {
        return memory_interfaces;
    }

    public void addMemory_interface(Memory_interface memory_interface) {
        this.memory_interfaces.add(memory_interface);
    }
    public List<Machine> getMachines() {
        return machines;
    }

    public void addMachine(Machine machine) {
        this.machines.add(machine);
    }

}