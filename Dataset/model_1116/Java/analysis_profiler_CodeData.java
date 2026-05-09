





import java.util.List;
import java.util.ArrayList;

public class analysis_profiler_CodeData  {

    private String blockName;
    private String nol;



    public analysis_profiler_CodeData(
        String blockName,        String nol    ) {
        this.blockName = blockName;
        this.nol = nol;
    }


    public String getBlockname() {
        return blockName;
    }

    public void setBlockname(String blockName) {
        this.blockName = blockName;
    }
    public String getNol() {
        return nol;
    }

    public void setNol(String nol) {
        this.nol = nol;
    }


}