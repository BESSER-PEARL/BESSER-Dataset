





import java.util.List;
import java.util.ArrayList;

public class Operating_System  {

    private int PROC_DATA_POINTER;
    private int PROC_BASE_REGISTER;
    private int PAGE_SIZE;
    private int INSTRUCTION_REGISTER;
    private None taskManager;
    private None dispatcher;
    private None prompt;
    private None cpu;
    private int PROC_BASE_POINTER;
    private int NUMBER_OF_REGISTERS;
    private None device;
    private int QUANTUM;
    private None memory;
    private int MEMORY_SIZE;
    private None clock;
    private int PROCESS_ID_REGISTER;
    private None scheduler;
    private None hardDrive;
    private int PROC_LIMIT_REGISTER;



    public Operating_System(
        int PROC_DATA_POINTER,        int PROC_BASE_REGISTER,        int PAGE_SIZE,        int INSTRUCTION_REGISTER,        None taskManager,        None dispatcher,        None prompt,        None cpu,        int PROC_BASE_POINTER,        int NUMBER_OF_REGISTERS,        None device,        int QUANTUM,        None memory,        int MEMORY_SIZE,        None clock,        int PROCESS_ID_REGISTER,        None scheduler,        None hardDrive,        int PROC_LIMIT_REGISTER    ) {
        this.PROC_DATA_POINTER = PROC_DATA_POINTER;
        this.PROC_BASE_REGISTER = PROC_BASE_REGISTER;
        this.PAGE_SIZE = PAGE_SIZE;
        this.INSTRUCTION_REGISTER = INSTRUCTION_REGISTER;
        this.taskManager = taskManager;
        this.dispatcher = dispatcher;
        this.prompt = prompt;
        this.cpu = cpu;
        this.PROC_BASE_POINTER = PROC_BASE_POINTER;
        this.NUMBER_OF_REGISTERS = NUMBER_OF_REGISTERS;
        this.device = device;
        this.QUANTUM = QUANTUM;
        this.memory = memory;
        this.MEMORY_SIZE = MEMORY_SIZE;
        this.clock = clock;
        this.PROCESS_ID_REGISTER = PROCESS_ID_REGISTER;
        this.scheduler = scheduler;
        this.hardDrive = hardDrive;
        this.PROC_LIMIT_REGISTER = PROC_LIMIT_REGISTER;
    }


    public int getProc_data_pointer() {
        return PROC_DATA_POINTER;
    }

    public void setProc_data_pointer(int PROC_DATA_POINTER) {
        this.PROC_DATA_POINTER = PROC_DATA_POINTER;
    }
    public int getProc_base_register() {
        return PROC_BASE_REGISTER;
    }

    public void setProc_base_register(int PROC_BASE_REGISTER) {
        this.PROC_BASE_REGISTER = PROC_BASE_REGISTER;
    }
    public int getPage_size() {
        return PAGE_SIZE;
    }

    public void setPage_size(int PAGE_SIZE) {
        this.PAGE_SIZE = PAGE_SIZE;
    }
    public int getInstruction_register() {
        return INSTRUCTION_REGISTER;
    }

    public void setInstruction_register(int INSTRUCTION_REGISTER) {
        this.INSTRUCTION_REGISTER = INSTRUCTION_REGISTER;
    }
    public None getTaskmanager() {
        return taskManager;
    }

    public void setTaskmanager(None taskManager) {
        this.taskManager = taskManager;
    }
    public None getDispatcher() {
        return dispatcher;
    }

    public void setDispatcher(None dispatcher) {
        this.dispatcher = dispatcher;
    }
    public None getPrompt() {
        return prompt;
    }

    public void setPrompt(None prompt) {
        this.prompt = prompt;
    }
    public None getCpu() {
        return cpu;
    }

    public void setCpu(None cpu) {
        this.cpu = cpu;
    }
    public int getProc_base_pointer() {
        return PROC_BASE_POINTER;
    }

    public void setProc_base_pointer(int PROC_BASE_POINTER) {
        this.PROC_BASE_POINTER = PROC_BASE_POINTER;
    }
    public int getNumber_of_registers() {
        return NUMBER_OF_REGISTERS;
    }

    public void setNumber_of_registers(int NUMBER_OF_REGISTERS) {
        this.NUMBER_OF_REGISTERS = NUMBER_OF_REGISTERS;
    }
    public None getDevice() {
        return device;
    }

    public void setDevice(None device) {
        this.device = device;
    }
    public int getQuantum() {
        return QUANTUM;
    }

    public void setQuantum(int QUANTUM) {
        this.QUANTUM = QUANTUM;
    }
    public None getMemory() {
        return memory;
    }

    public void setMemory(None memory) {
        this.memory = memory;
    }
    public int getMemory_size() {
        return MEMORY_SIZE;
    }

    public void setMemory_size(int MEMORY_SIZE) {
        this.MEMORY_SIZE = MEMORY_SIZE;
    }
    public None getClock() {
        return clock;
    }

    public void setClock(None clock) {
        this.clock = clock;
    }
    public int getProcess_id_register() {
        return PROCESS_ID_REGISTER;
    }

    public void setProcess_id_register(int PROCESS_ID_REGISTER) {
        this.PROCESS_ID_REGISTER = PROCESS_ID_REGISTER;
    }
    public None getScheduler() {
        return scheduler;
    }

    public void setScheduler(None scheduler) {
        this.scheduler = scheduler;
    }
    public None getHarddrive() {
        return hardDrive;
    }

    public void setHarddrive(None hardDrive) {
        this.hardDrive = hardDrive;
    }
    public int getProc_limit_register() {
        return PROC_LIMIT_REGISTER;
    }

    public void setProc_limit_register(int PROC_LIMIT_REGISTER) {
        this.PROC_LIMIT_REGISTER = PROC_LIMIT_REGISTER;
    }


}