





import java.util.List;
import java.util.ArrayList;

public class sADL_StartWriteStatement extends SadlModelElement {

    private String write;
    private String dataOnly;



    public sADL_StartWriteStatement(
        String write,        String dataOnly    ) {
        super(
        );
        this.write = write;
        this.dataOnly = dataOnly;
    }


    public String getWrite() {
        return write;
    }

    public void setWrite(String write) {
        this.write = write;
    }
    public String getDataonly() {
        return dataOnly;
    }

    public void setDataonly(String dataOnly) {
        this.dataOnly = dataOnly;
    }


}