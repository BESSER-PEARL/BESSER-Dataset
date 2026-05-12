





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_Echo extends MiscellaneousTask {

    private String file;
    private String message;
    private String append;



    public MavenMaven_Echo(
        String file,        String message,        String append    ) {
        super(
        );
        this.file = file;
        this.message = message;
        this.append = append;
    }


    public String getFile() {
        return file;
    }

    public void setFile(String file) {
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


}