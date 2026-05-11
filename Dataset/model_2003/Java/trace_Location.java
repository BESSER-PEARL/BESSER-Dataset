





import java.util.List;
import java.util.ArrayList;

public class trace_Location  {

    private String file;
    private String function;
    private String line;



    public trace_Location(
        String file,        String function,        String line    ) {
        this.file = file;
        this.function = function;
        this.line = line;
    }


    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
    }
    public String getFunction() {
        return function;
    }

    public void setFunction(String function) {
        this.function = function;
    }
    public String getLine() {
        return line;
    }

    public void setLine(String line) {
        this.line = line;
    }


}