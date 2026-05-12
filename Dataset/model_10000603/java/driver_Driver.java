





import java.util.List;
import java.util.ArrayList;

public class driver_Driver  {

    private None dispatcher;
    private String threads;
    private None cpus;
    private int cacheSize;
    private None scheduler;
    private None loader;
    private None disk;
    private int ramSize;
    private int executeTimes;
    private int registerSize;
    private int idleTimes;
    private None taskManager;





    private List<cpu_CPU> cpu_cpus;




    private pcb_TaskManager pcb_taskmanager;


    public driver_Driver(
        None dispatcher,        String threads,        None cpus,        int cacheSize,        None scheduler,        None loader,        None disk,        int ramSize,        int executeTimes,        int registerSize,        int idleTimes,        None taskManager    ) {
        this.dispatcher = dispatcher;
        this.threads = threads;
        this.cpus = cpus;
        this.cacheSize = cacheSize;
        this.scheduler = scheduler;
        this.loader = loader;
        this.disk = disk;
        this.ramSize = ramSize;
        this.executeTimes = executeTimes;
        this.registerSize = registerSize;
        this.idleTimes = idleTimes;
        this.taskManager = taskManager;
        this.cpu_cpus = new ArrayList<>();
    }

    public driver_Driver(
        None dispatcher,        String threads,        None cpus,        int cacheSize,        None scheduler,        None loader,        None disk,        int ramSize,        int executeTimes,        int registerSize,        int idleTimes,        None taskManager        ArrayList<cpu_CPU> cpu_cpus    ) {
        this.dispatcher = dispatcher;
        this.threads = threads;
        this.cpus = cpus;
        this.cacheSize = cacheSize;
        this.scheduler = scheduler;
        this.loader = loader;
        this.disk = disk;
        this.ramSize = ramSize;
        this.executeTimes = executeTimes;
        this.registerSize = registerSize;
        this.idleTimes = idleTimes;
        this.taskManager = taskManager;
        this.cpu_cpus = cpu_cpus;
    }

    public None getDispatcher() {
        return dispatcher;
    }

    public void setDispatcher(None dispatcher) {
        this.dispatcher = dispatcher;
    }
    public String getThreads() {
        return threads;
    }

    public void setThreads(String threads) {
        this.threads = threads;
    }
    public None getCpus() {
        return cpus;
    }

    public void setCpus(None cpus) {
        this.cpus = cpus;
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
    public None getLoader() {
        return loader;
    }

    public void setLoader(None loader) {
        this.loader = loader;
    }
    public None getDisk() {
        return disk;
    }

    public void setDisk(None disk) {
        this.disk = disk;
    }
    public int getRamsize() {
        return ramSize;
    }

    public void setRamsize(int ramSize) {
        this.ramSize = ramSize;
    }
    public int getExecutetimes() {
        return executeTimes;
    }

    public void setExecutetimes(int executeTimes) {
        this.executeTimes = executeTimes;
    }
    public int getRegistersize() {
        return registerSize;
    }

    public void setRegistersize(int registerSize) {
        this.registerSize = registerSize;
    }
    public int getIdletimes() {
        return idleTimes;
    }

    public void setIdletimes(int idleTimes) {
        this.idleTimes = idleTimes;
    }
    public None getTaskmanager() {
        return taskManager;
    }

    public void setTaskmanager(None taskManager) {
        this.taskManager = taskManager;
    }

    public List<cpu_CPU> getCpu_cpus() {
        return cpu_cpus;
    }

    public void addCpu_cpu(Cpu_cpu cpu_cpu) {
        this.cpu_cpus.add(cpu_cpu);
    }
    public pcb_TaskManager getPcb_taskmanager() {
        return pcb_taskmanager;
    }

    public void setPcb_taskmanager(pcb_TaskManager pcb_taskmanager) {
        this.pcb_taskmanager = pcb_taskmanager;
    }

}