





import java.util.List;
import java.util.ArrayList;

public class sADL_EndWriteStatement extends SadlModelElement {

    private String filename;



    public sADL_EndWriteStatement(
        String filename    ) {
        super(
        );
        this.filename = filename;
    }


    public String getFilename() {
        return filename;
    }

    public void setFilename(String filename) {
        this.filename = filename;
    }


}