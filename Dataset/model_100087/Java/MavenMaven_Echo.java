





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_Echo extends MiscellaneousTask {

    private String file;
    private String append;
    private String message;



    public MavenMaven_Echo(
        String file,        String append,        String message    ) {
        super(
        );
        this.file = file;
        this.append = append;
        this.message = message;
    }


    public String getFile() {
        return file;
    }

    public void setFile(String file) {
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


}