





import java.util.List;
import java.util.ArrayList;

public class driver_Driver  {

    private int ramSize;
    private None dispatcher;
    private int cacheSize;
    private None scheduler;
    private None cpus;
    private int idleTimes;
    private String threads;
    private int executeTimes;
    private None loader;
    private int registerSize;
    private None disk;
    private None taskManager;





    private pcb_TaskManager pcb_taskmanager;




    private List<cpu_CPU> cpu_cpus;


    public driver_Driver(
        int ramSize,        None dispatcher,        int cacheSize,        None scheduler,        None cpus,        int idleTimes,        String threads,        int executeTimes,        None loader,        int registerSize,        None disk,        None taskManager    ) {
        this.ramSize = ramSize;
        this.dispatcher = dispatcher;
        this.cacheSize = cacheSize;
        this.scheduler = scheduler;
        this.cpus = cpus;
        this.idleTimes = idleTimes;
        this.threads = threads;
        this.executeTimes = executeTimes;
        this.loader = loader;
        this.registerSize = registerSize;
        this.disk = disk;
        this.taskManager = taskManager;
        this.cpu_cpus = new ArrayList<>();
    }

    public driver_Driver(
        int ramSize,        None dispatcher,        int cacheSize,        None scheduler,        None cpus,        int idleTimes,        String threads,        int executeTimes,        None loader,        int registerSize,        None disk,        None taskManager        ArrayList<cpu_CPU> cpu_cpus    ) {
        this.ramSize = ramSize;
        this.dispatcher = dispatcher;
        this.cacheSize = cacheSize;
        this.scheduler = scheduler;
        this.cpus = cpus;
        this.idleTimes = idleTimes;
        this.threads = threads;
        this.executeTimes = executeTimes;
        this.loader = loader;
        this.registerSize = registerSize;
        this.disk = disk;
        this.taskManager = taskManager;
        this.cpu_cpus = cpu_cpus;
    }

    public int getRamsize() {
        return ramSize;
    }

    public void setRamsize(int ramSize) {
        this.ramSize = ramSize;
    }
    public None getDispatcher() {
        return dispatcher;
    }

    public void setDispatcher(None dispatcher) {
        this.dispatcher = dispatcher;
    }
    public int getCachesize() {
        return cacheSize;
    }

    public void setCachesize(int cacheSize) {
        this.cacheSize = cacheSize;
    }
    public None getScheduler() {
        return scheduler;
    }

    public void setScheduler(None scheduler) {
        this.scheduler = scheduler;
    }
    public None getCpus() {
        return cpus;
    }

    public void setCpus(None cpus) {
        this.cpus = cpus;
    }
    public int getIdletimes() {
        return idleTimes;
    }

    public void setIdletimes(int idleTimes) {
        this.idleTimes = idleTimes;
    }
    public String getThreads() {
        return threads;
    }

    public void setThreads(String threads) {
        this.threads = threads;
    }
    public int getExecutetimes() {
        return executeTimes;
    }

    public void setExecutetimes(int executeTimes) {
        this.executeTimes = executeTimes;
    }
    public None getLoader() {
        return loader;
    }

    public void setLoader(None loader) {
        this.loader = loader;
    }
    public int getRegistersize() {
        return registerSize;
    }

    public void setRegistersize(int registerSize) {
        this.registerSize = registerSize;
    }
    public None getDisk() {
        return disk;
    }

    public void setDisk(None disk) {
        this.disk = disk;
    }
    public None getTaskmanager() {
        return taskManager;
    }

    public void setTaskmanager(None taskManager) {
        this.taskManager = taskManager;
    }

    public pcb_TaskManager getPcb_taskmanager() {
        return pcb_taskmanager;
    }

    public void setPcb_taskmanager(pcb_TaskManager pcb_taskmanager) {
        this.pcb_taskmanager = pcb_taskmanager;
    }
    public List<cpu_CPU> getCpu_cpus() {
        return cpu_cpus;
    }

    public void addCpu_cpu(Cpu_cpu cpu_cpu) {
        this.cpu_cpus.add(cpu_cpu);
    }

}