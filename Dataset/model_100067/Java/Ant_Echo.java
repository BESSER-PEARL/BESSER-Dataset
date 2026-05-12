





import java.util.List;
import java.util.ArrayList;

public class Ant_Echo extends MiscellaneousTask {

    private String append;
    private String message;
    private String file;



    public Ant_Echo(
        String append,        String message,        String file    ) {
        super(
        );
        this.append = append;
        this.message = message;
        this.file = file;
    }


    public String getAppend() {
        return append;
    }

    public void setAppend(String append) {
        this.append = append;
    }
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
    }


}