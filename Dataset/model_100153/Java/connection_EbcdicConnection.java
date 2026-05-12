





import java.util.List;
import java.util.ArrayList;

public class connection_EbcdicConnection extends FileConnection {

    private String DataFile;
    private String MidFile;



    public connection_EbcdicConnection(
        String DataFile,        String MidFile    ) {
        super(
        );
        this.DataFile = DataFile;
        this.MidFile = MidFile;
    }


    public String getDatafile() {
        return DataFile;
    }

    public void setDatafile(String DataFile) {
        this.DataFile = DataFile;
    }
    public String getMidfile() {
        return MidFile;
    }

    public void setMidfile(String MidFile) {
        this.MidFile = MidFile;
    }


}