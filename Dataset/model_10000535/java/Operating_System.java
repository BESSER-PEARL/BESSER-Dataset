





import java.util.List;
import java.util.ArrayList;

public class Operating_System  {

    private int INSTRUCTION_REGISTER;
    private None hardDrive;
    private int QUANTUM;
    private int PROCESS_ID_REGISTER;
    private int NUMBER_OF_REGISTERS;
    private None memory;
    private None taskManager;
    private None dispatcher;
    private None cpu;
    private int PROC_BASE_POINTER;
    private None device;
    private None clock;
    private None scheduler;
    private int MEMORY_SIZE;
    private int PROC_DATA_POINTER;
    private int PAGE_SIZE;
    private None prompt;
    private int PROC_BASE_REGISTER;
    private int PROC_LIMIT_REGISTER;





    private Task_Manager task_manager;




    private ProcessTableModel processtablemodel;




    private Instruction_Yield instruction_yield;




    private Instruction_Out instruction_out;




    private Instruction_IO instruction_io;




    private Main main;




    private Instruction_Calculate instruction_calculate;




    private Instruction_Exit instruction_exit;


    public Operating_System(
        int INSTRUCTION_REGISTER,        None hardDrive,        int QUANTUM,        int PROCESS_ID_REGISTER,        int NUMBER_OF_REGISTERS,        None memory,        None taskManager,        None dispatcher,        None cpu,        int PROC_BASE_POINTER,        None device,        None clock,        None scheduler,        int MEMORY_SIZE,        int PROC_DATA_POINTER,        int PAGE_SIZE,        None prompt,        int PROC_BASE_REGISTER,        int PROC_LIMIT_REGISTER    ) {
        this.INSTRUCTION_REGISTER = INSTRUCTION_REGISTER;
        this.hardDrive = hardDrive;
        this.QUANTUM = QUANTUM;
        this.PROCESS_ID_REGISTER = PROCESS_ID_REGISTER;
        this.NUMBER_OF_REGISTERS = NUMBER_OF_REGISTERS;
        this.memory = memory;
        this.taskManager = taskManager;
        this.dispatcher = dispatcher;
        this.cpu = cpu;
        this.PROC_BASE_POINTER = PROC_BASE_POINTER;
        this.device = device;
        this.clock = clock;
        this.scheduler = scheduler;
        this.MEMORY_SIZE = MEMORY_SIZE;
        this.PROC_DATA_POINTER = PROC_DATA_POINTER;
        this.PAGE_SIZE = PAGE_SIZE;
        this.prompt = prompt;
        this.PROC_BASE_REGISTER = PROC_BASE_REGISTER;
        this.PROC_LIMIT_REGISTER = PROC_LIMIT_REGISTER;
    }


    public int getInstruction_register() {
        return INSTRUCTION_REGISTER;
    }

    public void setInstruction_register(int INSTRUCTION_REGISTER) {
        this.INSTRUCTION_REGISTER = INSTRUCTION_REGISTER;
    }
    public None getHarddrive() {
        return hardDrive;
    }

    public void setHarddrive(None hardDrive) {
        this.hardDrive = hardDrive;
    }
    public int getQuantum() {
        return QUANTUM;
    }

    public void setQuantum(int QUANTUM) {
        this.QUANTUM = QUANTUM;
    }
    public int getProcess_id_register() {
        return PROCESS_ID_REGISTER;
    }

    public void setProcess_id_register(int PROCESS_ID_REGISTER) {
        this.PROCESS_ID_REGISTER = PROCESS_ID_REGISTER;
    }
    public int getNumber_of_registers() {
        return NUMBER_OF_REGISTERS;
    }

    public void setNumber_of_registers(int NUMBER_OF_REGISTERS) {
        this.NUMBER_OF_REGISTERS = NUMBER_OF_REGISTERS;
    }
    public None getMemory() {
        return memory;
    }

    public void setMemory(None memory) {
        this.memory = memory;
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
    public None getDevice() {
        return device;
    }

    public void setDevice(None device) {
        this.device = device;
    }
    public None getClock() {
        return clock;
    }

    public void setClock(None clock) {
        this.clock = clock;
    }
    public None getScheduler() {
        return scheduler;
    }

    public void setScheduler(None scheduler) {
        this.scheduler = scheduler;
    }
    public int getMemory_size() {
        return MEMORY_SIZE;
    }

    public void setMemory_size(int MEMORY_SIZE) {
        this.MEMORY_SIZE = MEMORY_SIZE;
    }
    public int getProc_data_pointer() {
        return PROC_DATA_POINTER;
    }

    public void setProc_data_pointer(int PROC_DATA_POINTER) {
        this.PROC_DATA_POINTER = PROC_DATA_POINTER;
    }
    public int getPage_size() {
        return PAGE_SIZE;
    }

    public void setPage_size(int PAGE_SIZE) {
        this.PAGE_SIZE = PAGE_SIZE;
    }
    public None getPrompt() {
        return prompt;
    }

    public void setPrompt(None prompt) {
        this.prompt = prompt;
    }
    public int getProc_base_register() {
        return PROC_BASE_REGISTER;
    }

    public void setProc_base_register(int PROC_BASE_REGISTER) {
        this.PROC_BASE_REGISTER = PROC_BASE_REGISTER;
    }
    public int getProc_limit_register() {
        return PROC_LIMIT_REGISTER;
    }

    public void setProc_limit_register(int PROC_LIMIT_REGISTER) {
        this.PROC_LIMIT_REGISTER = PROC_LIMIT_REGISTER;
    }

    public Task_Manager getTask_manager() {
        return task_manager;
    }

    public void setTask_manager(Task_Manager task_manager) {
        this.task_manager = task_manager;
    }
    public ProcessTableModel getProcesstablemodel() {
        return processtablemodel;
    }

    public void setProcesstablemodel(ProcessTableModel processtablemodel) {
        this.processtablemodel = processtablemodel;
    }
    public Instruction_Yield getInstruction_yield() {
        return instruction_yield;
    }

    public void setInstruction_yield(Instruction_Yield instruction_yield) {
        this.instruction_yield = instruction_yield;
    }
    public Instruction_Out getInstruction_out() {
        return instruction_out;
    }

    public void setInstruction_out(Instruction_Out instruction_out) {
        this.instruction_out = instruction_out;
    }
    public Instruction_IO getInstruction_io() {
        return instruction_io;
    }

    public void setInstruction_io(Instruction_IO instruction_io) {
        this.instruction_io = instruction_io;
    }
    public Main getMain() {
        return main;
    }

    public void setMain(Main main) {
        this.main = main;
    }
    public Instruction_Calculate getInstruction_calculate() {
        return instruction_calculate;
    }

    public void setInstruction_calculate(Instruction_Calculate instruction_calculate) {
        this.instruction_calculate = instruction_calculate;
    }
    public Instruction_Exit getInstruction_exit() {
        return instruction_exit;
    }

    public void setInstruction_exit(Instruction_Exit instruction_exit) {
        this.instruction_exit = instruction_exit;
    }

}