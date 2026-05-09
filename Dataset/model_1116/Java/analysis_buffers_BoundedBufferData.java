





import java.util.List;
import java.util.ArrayList;

public class analysis_buffers_BoundedBufferData  {

    private int bitSize;
    private int tokenSize;



    public analysis_buffers_BoundedBufferData(
        int bitSize,        int tokenSize    ) {
        this.bitSize = bitSize;
        this.tokenSize = tokenSize;
    }


    public int getBitsize() {
        return bitSize;
    }

    public void setBitsize(int bitSize) {
        this.bitSize = bitSize;
    }
    public int getTokensize() {
        return tokenSize;
    }

    public void setTokensize(int tokenSize) {
        this.tokenSize = tokenSize;
    }


}