





import java.util.List;
import java.util.ArrayList;

public class checkers_PlaySound  {

    private String filename;
    private int EXTERNAL_BUFFER_SIZE;



    public checkers_PlaySound(
        String filename,        int EXTERNAL_BUFFER_SIZE    ) {
        this.filename = filename;
        this.EXTERNAL_BUFFER_SIZE = EXTERNAL_BUFFER_SIZE;
    }


    public String getFilename() {
        return filename;
    }

    public void setFilename(String filename) {
        this.filename = filename;
    }
    public int getExternal_buffer_size() {
        return EXTERNAL_BUFFER_SIZE;
    }

    public void setExternal_buffer_size(int EXTERNAL_BUFFER_SIZE) {
        this.EXTERNAL_BUFFER_SIZE = EXTERNAL_BUFFER_SIZE;
    }


}