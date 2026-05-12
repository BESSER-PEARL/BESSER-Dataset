





import java.util.List;
import java.util.ArrayList;

public class interpreter_RunTimeStack  {

    private String runStack;
    private int framePointers;



    public interpreter_RunTimeStack(
        String runStack,        int framePointers    ) {
        this.runStack = runStack;
        this.framePointers = framePointers;
    }


    public String getRunstack() {
        return runStack;
    }

    public void setRunstack(String runStack) {
        this.runStack = runStack;
    }
    public int getFramepointers() {
        return framePointers;
    }

    public void setFramepointers(int framePointers) {
        this.framePointers = framePointers;
    }


}