





import java.util.List;
import java.util.ArrayList;

public class MARTE_HwMemory_HwDrive extends HwMemory {






    private HwMemory_HwRAM hwmemory_hwram;




    private NFP_DataSize nfp_datasize;


    public MARTE_HwMemory_HwDrive(
    ) {
        super(
        );
    }



    public HwMemory_HwRAM getHwmemory_hwram() {
        return hwmemory_hwram;
    }

    public void setHwmemory_hwram(HwMemory_HwRAM hwmemory_hwram) {
        this.hwmemory_hwram = hwmemory_hwram;
    }
    public NFP_DataSize getNfp_datasize() {
        return nfp_datasize;
    }

    public void setNfp_datasize(NFP_DataSize nfp_datasize) {
        this.nfp_datasize = nfp_datasize;
    }

}