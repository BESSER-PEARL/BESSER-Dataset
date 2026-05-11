





import java.util.List;
import java.util.ArrayList;

public class MARTE_HwStorageManager_HwMMU extends HwStorageManager {

    private String virtualAddrSpace;
    private String memoryProtection;
    private String physicalAddrSpace;
    private String nbEntries;





    private List<HwMemory_HwCache> hwmemory_hwcaches;


    public MARTE_HwStorageManager_HwMMU(
        String virtualAddrSpace,        String memoryProtection,        String physicalAddrSpace,        String nbEntries    ) {
        super(
        );
        this.virtualAddrSpace = virtualAddrSpace;
        this.memoryProtection = memoryProtection;
        this.physicalAddrSpace = physicalAddrSpace;
        this.nbEntries = nbEntries;
        this.hwmemory_hwcaches = new ArrayList<>();
    }

    public MARTE_HwStorageManager_HwMMU(
        String virtualAddrSpace,        String memoryProtection,        String physicalAddrSpace,        String nbEntries        ArrayList<HwMemory_HwCache> hwmemory_hwcaches    ) {
        this.virtualAddrSpace = virtualAddrSpace;
        this.memoryProtection = memoryProtection;
        this.physicalAddrSpace = physicalAddrSpace;
        this.nbEntries = nbEntries;
        this.hwmemory_hwcaches = hwmemory_hwcaches;
    }

    public String getVirtualaddrspace() {
        return virtualAddrSpace;
    }

    public void setVirtualaddrspace(String virtualAddrSpace) {
        this.virtualAddrSpace = virtualAddrSpace;
    }
    public String getMemoryprotection() {
        return memoryProtection;
    }

    public void setMemoryprotection(String memoryProtection) {
        this.memoryProtection = memoryProtection;
    }
    public String getPhysicaladdrspace() {
        return physicalAddrSpace;
    }

    public void setPhysicaladdrspace(String physicalAddrSpace) {
        this.physicalAddrSpace = physicalAddrSpace;
    }
    public String getNbentries() {
        return nbEntries;
    }

    public void setNbentries(String nbEntries) {
        this.nbEntries = nbEntries;
    }

    public List<HwMemory_HwCache> getHwmemory_hwcaches() {
        return hwmemory_hwcaches;
    }

    public void addHwmemory_hwcache(Hwmemory_hwcache hwmemory_hwcache) {
        this.hwmemory_hwcaches.add(hwmemory_hwcache);
    }

}