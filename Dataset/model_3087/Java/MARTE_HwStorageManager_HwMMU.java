





import java.util.List;
import java.util.ArrayList;

public class MARTE_HwStorageManager_HwMMU extends HwStorageManager {






    private NFP_DataSize nfp_datasize;




    private NFP_Natural nfp_natural;




    private NFP_DataSize nfp_datasize;




    private List<HwMemory_HwCache> hwmemory_hwcaches;


    public MARTE_HwStorageManager_HwMMU(
    ) {
        super(
        );
        this.hwmemory_hwcaches = new ArrayList<>();
    }

    public MARTE_HwStorageManager_HwMMU(
        ArrayList<HwMemory_HwCache> hwmemory_hwcaches    ) {
        this.hwmemory_hwcaches = hwmemory_hwcaches;
    }


    public NFP_DataSize getNfp_datasize() {
        return nfp_datasize;
    }

    public void setNfp_datasize(NFP_DataSize nfp_datasize) {
        this.nfp_datasize = nfp_datasize;
    }
    public NFP_Natural getNfp_natural() {
        return nfp_natural;
    }

    public void setNfp_natural(NFP_Natural nfp_natural) {
        this.nfp_natural = nfp_natural;
    }
    public NFP_DataSize getNfp_datasize() {
        return nfp_datasize;
    }

    public void setNfp_datasize(NFP_DataSize nfp_datasize) {
        this.nfp_datasize = nfp_datasize;
    }
    public List<HwMemory_HwCache> getHwmemory_hwcaches() {
        return hwmemory_hwcaches;
    }

    public void addHwmemory_hwcache(Hwmemory_hwcache hwmemory_hwcache) {
        this.hwmemory_hwcaches.add(hwmemory_hwcache);
    }

}