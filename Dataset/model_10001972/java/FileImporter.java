





import java.util.List;
import java.util.ArrayList;

public class FileImporter  {

    private String INITIAL_DATAFILE;



    public FileImporter(
        String INITIAL_DATAFILE    ) {
        this.INITIAL_DATAFILE = INITIAL_DATAFILE;
    }


    public String getInitial_datafile() {
        return INITIAL_DATAFILE;
    }

    public void setInitial_datafile(String INITIAL_DATAFILE) {
        this.INITIAL_DATAFILE = INITIAL_DATAFILE;
    }


}