





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_Echo extends MiscellaneousTask {

    private String append;
    private String file;
    private String message;



    public MavenMaven_Echo(
        String append,        String file,        String message    ) {
        super(
        );
        this.append = append;
        this.file = file;
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
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }


}