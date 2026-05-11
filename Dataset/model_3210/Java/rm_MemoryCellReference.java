





import java.util.List;
import java.util.ArrayList;

public class rm_MemoryCellReference  {

    private int endCellIndex;
    private int startCellIndex;





    private rm_Device rm_device;


    public rm_MemoryCellReference(
        int endCellIndex,        int startCellIndex    ) {
        this.endCellIndex = endCellIndex;
        this.startCellIndex = startCellIndex;
    }


    public int getEndcellindex() {
        return endCellIndex;
    }

    public void setEndcellindex(int endCellIndex) {
        this.endCellIndex = endCellIndex;
    }
    public int getStartcellindex() {
        return startCellIndex;
    }

    public void setStartcellindex(int startCellIndex) {
        this.startCellIndex = startCellIndex;
    }

    public rm_Device getRm_device() {
        return rm_device;
    }

    public void setRm_device(rm_Device rm_device) {
        this.rm_device = rm_device;
    }

}