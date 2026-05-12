





import java.util.List;
import java.util.ArrayList;

public class Process  {

    private None processState;
    private int memoryUseage;
    private String registers;
    private String name;





    private Task_Manager task_manager;




    private ProcessTableModel processtablemodel;




    private Page page;




    private Instruction_IO instruction_io;




    private Instruction_Exit instruction_exit;


    public Process(
        None processState,        int memoryUseage,        String registers,        String name    ) {
        this.processState = processState;
        this.memoryUseage = memoryUseage;
        this.registers = registers;
        this.name = name;
    }


    public None getProcessstate() {
        return processState;
    }

    public void setProcessstate(None processState) {
        this.processState = processState;
    }
    public int getMemoryuseage() {
        return memoryUseage;
    }

    public void setMemoryuseage(int memoryUseage) {
        this.memoryUseage = memoryUseage;
    }
    public String getRegisters() {
        return registers;
    }

    public void setRegisters(String registers) {
        this.registers = registers;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public Page getPage() {
        return page;
    }

    public void setPage(Page page) {
        this.page = page;
    }
    public Instruction_IO getInstruction_io() {
        return instruction_io;
    }

    public void setInstruction_io(Instruction_IO instruction_io) {
        this.instruction_io = instruction_io;
    }
    public Instruction_Exit getInstruction_exit() {
        return instruction_exit;
    }

    public void setInstruction_exit(Instruction_Exit instruction_exit) {
        this.instruction_exit = instruction_exit;
    }

}