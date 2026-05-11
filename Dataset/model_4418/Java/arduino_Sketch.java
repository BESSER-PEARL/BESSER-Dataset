





import java.util.List;
import java.util.ArrayList;

public class arduino_Sketch  {

    private boolean defineSystem;
    private String name;
    private String hardware;





    private List<arduino_Handler> arduino_handlers;




    private List<arduino_Task> arduino_tasks;




    private List<arduino_Interrupt> arduino_interrupts;




    private arduino_SystemDefinition arduino_systemdefinition;




    private List<arduino_LoopItem> arduino_loopitems;




    private List<arduino_AbstractDevice> arduino_abstractdevices;




    private List<arduino_Poll> arduino_polls;


    public arduino_Sketch(
        boolean defineSystem,        String name,        String hardware    ) {
        this.defineSystem = defineSystem;
        this.name = name;
        this.hardware = hardware;
        this.arduino_handlers = new ArrayList<>();
        this.arduino_tasks = new ArrayList<>();
        this.arduino_interrupts = new ArrayList<>();
        this.arduino_loopitems = new ArrayList<>();
        this.arduino_abstractdevices = new ArrayList<>();
        this.arduino_polls = new ArrayList<>();
    }

    public arduino_Sketch(
        boolean defineSystem,        String name,        String hardware        ArrayList<arduino_Handler> arduino_handlers,        ArrayList<arduino_Task> arduino_tasks,        ArrayList<arduino_Interrupt> arduino_interrupts,        ArrayList<arduino_LoopItem> arduino_loopitems,        ArrayList<arduino_AbstractDevice> arduino_abstractdevices,        ArrayList<arduino_Poll> arduino_polls    ) {
        this.defineSystem = defineSystem;
        this.name = name;
        this.hardware = hardware;
        this.arduino_handlers = arduino_handlers;
        this.arduino_tasks = arduino_tasks;
        this.arduino_interrupts = arduino_interrupts;
        this.arduino_loopitems = arduino_loopitems;
        this.arduino_abstractdevices = arduino_abstractdevices;
        this.arduino_polls = arduino_polls;
    }

    public boolean getDefinesystem() {
        return defineSystem;
    }

    public void setDefinesystem(boolean defineSystem) {
        this.defineSystem = defineSystem;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getHardware() {
        return hardware;
    }

    public void setHardware(String hardware) {
        this.hardware = hardware;
    }

    public List<arduino_Handler> getArduino_handlers() {
        return arduino_handlers;
    }

    public void addArduino_handler(Arduino_handler arduino_handler) {
        this.arduino_handlers.add(arduino_handler);
    }
    public List<arduino_Task> getArduino_tasks() {
        return arduino_tasks;
    }

    public void addArduino_task(Arduino_task arduino_task) {
        this.arduino_tasks.add(arduino_task);
    }
    public List<arduino_Interrupt> getArduino_interrupts() {
        return arduino_interrupts;
    }

    public void addArduino_interrupt(Arduino_interrupt arduino_interrupt) {
        this.arduino_interrupts.add(arduino_interrupt);
    }
    public arduino_SystemDefinition getArduino_systemdefinition() {
        return arduino_systemdefinition;
    }

    public void setArduino_systemdefinition(arduino_SystemDefinition arduino_systemdefinition) {
        this.arduino_systemdefinition = arduino_systemdefinition;
    }
    public List<arduino_LoopItem> getArduino_loopitems() {
        return arduino_loopitems;
    }

    public void addArduino_loopitem(Arduino_loopitem arduino_loopitem) {
        this.arduino_loopitems.add(arduino_loopitem);
    }
    public List<arduino_AbstractDevice> getArduino_abstractdevices() {
        return arduino_abstractdevices;
    }

    public void addArduino_abstractdevice(Arduino_abstractdevice arduino_abstractdevice) {
        this.arduino_abstractdevices.add(arduino_abstractdevice);
    }
    public List<arduino_Poll> getArduino_polls() {
        return arduino_polls;
    }

    public void addArduino_poll(Arduino_poll arduino_poll) {
        this.arduino_polls.add(arduino_poll);
    }

}