





import java.util.List;
import java.util.ArrayList;

public class simulink_buffer_BufferFunction extends EmbeddedFunction {

    private int bufferSize;



    public simulink_buffer_BufferFunction(
        int bufferSize    ) {
        super(
        );
        this.bufferSize = bufferSize;
    }


    public int getBuffersize() {
        return bufferSize;
    }

    public void setBuffersize(int bufferSize) {
        this.bufferSize = bufferSize;
    }


}