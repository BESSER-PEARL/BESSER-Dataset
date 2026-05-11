





import java.util.List;
import java.util.ArrayList;

public class idl_File_Marker extends Preproc {

    private String file;



    public idl_File_Marker(
        String file    ) {
        super(
        );
        this.file = file;
    }


    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
    }


}