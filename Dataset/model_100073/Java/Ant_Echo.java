





import java.util.List;
import java.util.ArrayList;

public class Ant_Echo extends MiscellaneousTask {

    private String message;
    private String append;
    private String file;



    public Ant_Echo(
        String message,        String append,        String file    ) {
        super(
        );
        this.message = message;
        this.append = append;
        this.file = file;
    }


    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public String getAppend() {
        return append;
    }

    public void setAppend(String append) {
        this.append = append;
    }
    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
    }


}