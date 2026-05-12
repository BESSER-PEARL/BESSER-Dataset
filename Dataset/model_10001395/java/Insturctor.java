





import java.util.List;
import java.util.ArrayList;

public class Insturctor  {

    private String INfilename;





    private FileBinary filebinary;


    public Insturctor(
        String INfilename    ) {
        this.INfilename = INfilename;
    }


    public String getInfilename() {
        return INfilename;
    }

    public void setInfilename(String INfilename) {
        this.INfilename = INfilename;
    }

    public FileBinary getFilebinary() {
        return filebinary;
    }

    public void setFilebinary(FileBinary filebinary) {
        this.filebinary = filebinary;
    }

}