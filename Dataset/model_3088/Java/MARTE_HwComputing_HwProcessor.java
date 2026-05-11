





import java.util.List;
import java.util.ArrayList;

public class MARTE_HwComputing_HwProcessor extends HwComputingResource {

    private String mips;
    private String nbFPUs;
    private String ipc;
    private String nbALUs;
    private String nbCores;
    private String nbStages;
    private String architecture;
    private String nbPipelines;





    private List<HwStorageManager_HwMMU> hwstoragemanager_hwmmus;


    public MARTE_HwComputing_HwProcessor(
        String mips,        String nbFPUs,        String ipc,        String nbALUs,        String nbCores,        String nbStages,        String architecture,        String nbPipelines    ) {
        super(
        );
        this.mips = mips;
        this.nbFPUs = nbFPUs;
        this.ipc = ipc;
        this.nbALUs = nbALUs;
        this.nbCores = nbCores;
        this.nbStages = nbStages;
        this.architecture = architecture;
        this.nbPipelines = nbPipelines;
        this.hwstoragemanager_hwmmus = new ArrayList<>();
    }

    public MARTE_HwComputing_HwProcessor(
        String mips,        String nbFPUs,        String ipc,        String nbALUs,        String nbCores,        String nbStages,        String architecture,        String nbPipelines        ArrayList<HwStorageManager_HwMMU> hwstoragemanager_hwmmus    ) {
        this.mips = mips;
        this.nbFPUs = nbFPUs;
        this.ipc = ipc;
        this.nbALUs = nbALUs;
        this.nbCores = nbCores;
        this.nbStages = nbStages;
        this.architecture = architecture;
        this.nbPipelines = nbPipelines;
        this.hwstoragemanager_hwmmus = hwstoragemanager_hwmmus;
    }

    public String getMips() {
        return mips;
    }

    public void setMips(String mips) {
        this.mips = mips;
    }
    public String getNbfpus() {
        return nbFPUs;
    }

    public void setNbfpus(String nbFPUs) {
        this.nbFPUs = nbFPUs;
    }
    public String getIpc() {
        return ipc;
    }

    public void setIpc(String ipc) {
        this.ipc = ipc;
    }
    public String getNbalus() {
        return nbALUs;
    }

    public void setNbalus(String nbALUs) {
        this.nbALUs = nbALUs;
    }
    public String getNbcores() {
        return nbCores;
    }

    public void setNbcores(String nbCores) {
        this.nbCores = nbCores;
    }
    public String getNbstages() {
        return nbStages;
    }

    public void setNbstages(String nbStages) {
        this.nbStages = nbStages;
    }
    public String getArchitecture() {
        return architecture;
    }

    public void setArchitecture(String architecture) {
        this.architecture = architecture;
    }
    public String getNbpipelines() {
        return nbPipelines;
    }

    public void setNbpipelines(String nbPipelines) {
        this.nbPipelines = nbPipelines;
    }

    public List<HwStorageManager_HwMMU> getHwstoragemanager_hwmmus() {
        return hwstoragemanager_hwmmus;
    }

    public void addHwstoragemanager_hwmmu(Hwstoragemanager_hwmmu hwstoragemanager_hwmmu) {
        this.hwstoragemanager_hwmmus.add(hwstoragemanager_hwmmu);
    }

}