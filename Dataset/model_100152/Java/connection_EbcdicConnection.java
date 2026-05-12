





import java.util.List;
import java.util.ArrayList;

public class connection_EbcdicConnection extends FileConnection {

    private String MidFile;
    private String DataFile;



    public connection_EbcdicConnection(
        String MidFile,        String DataFile    ) {
        super(
        );
        this.MidFile = MidFile;
        this.DataFile = DataFile;
    }


    public String getMidfile() {
        return MidFile;
    }

    public void setMidfile(String MidFile) {
        this.MidFile = MidFile;
    }
    public String getDatafile() {
        return DataFile;
    }

    public void setDatafile(String DataFile) {
        this.DataFile = DataFile;
    }


}