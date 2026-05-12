





import java.util.List;
import java.util.ArrayList;

public class file_FileUploadHandler  {

    private String SAVE_DIR;
    private String fileName1;



    public file_FileUploadHandler(
        String SAVE_DIR,        String fileName1    ) {
        this.SAVE_DIR = SAVE_DIR;
        this.fileName1 = fileName1;
    }


    public String getSave_dir() {
        return SAVE_DIR;
    }

    public void setSave_dir(String SAVE_DIR) {
        this.SAVE_DIR = SAVE_DIR;
    }
    public String getFilename1() {
        return fileName1;
    }

    public void setFilename1(String fileName1) {
        this.fileName1 = fileName1;
    }


}