





import java.util.List;
import java.util.ArrayList;

public class MARTE_HwMemory_HwDrive extends HwMemory {

    private String sectorSize;





    private HwMemory_HwRAM hwmemory_hwram;


    public MARTE_HwMemory_HwDrive(
        String sectorSize    ) {
        super(
        );
        this.sectorSize = sectorSize;
    }


    public String getSectorsize() {
        return sectorSize;
    }

    public void setSectorsize(String sectorSize) {
        this.sectorSize = sectorSize;
    }

    public HwMemory_HwRAM getHwmemory_hwram() {
        return hwmemory_hwram;
    }

    public void setHwmemory_hwram(HwMemory_HwRAM hwmemory_hwram) {
        this.hwmemory_hwram = hwmemory_hwram;
    }

}