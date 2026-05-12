





import java.util.List;
import java.util.ArrayList;

public class interpreter_ByteCodeLoader  {

    private String programMap;
    private None input;
    private int lineCount;



    public interpreter_ByteCodeLoader(
        String programMap,        None input,        int lineCount    ) {
        this.programMap = programMap;
        this.input = input;
        this.lineCount = lineCount;
    }


    public String getProgrammap() {
        return programMap;
    }

    public void setProgrammap(String programMap) {
        this.programMap = programMap;
    }
    public None getInput() {
        return input;
    }

    public void setInput(None input) {
        this.input = input;
    }
    public int getLinecount() {
        return lineCount;
    }

    public void setLinecount(int lineCount) {
        this.lineCount = lineCount;
    }


}