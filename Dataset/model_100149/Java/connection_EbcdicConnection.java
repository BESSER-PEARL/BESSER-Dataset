





import java.util.List;
import java.util.ArrayList;

public class connection_EbcdicConnection extends FileConnection {

    private String DataFile;
    private String SourceFileEnd;
    private String CodePage;
    private String SourceFileStart;
    private String MidFile;



    public connection_EbcdicConnection(
        String DataFile,        String SourceFileEnd,        String CodePage,        String SourceFileStart,        String MidFile    ) {
        super(
        );
        this.DataFile = DataFile;
        this.SourceFileEnd = SourceFileEnd;
        this.CodePage = CodePage;
        this.SourceFileStart = SourceFileStart;
        this.MidFile = MidFile;
    }


    public String getDatafile() {
        return DataFile;
    }

    public void setDatafile(String DataFile) {
        this.DataFile = DataFile;
    }
    public String getSourcefileend() {
        return SourceFileEnd;
    }

    public void setSourcefileend(String SourceFileEnd) {
        this.SourceFileEnd = SourceFileEnd;
    }
    public String getCodepage() {
        return CodePage;
    }

    public void setCodepage(String CodePage) {
        this.CodePage = CodePage;
    }
    public String getSourcefilestart() {
        return SourceFileStart;
    }

    public void setSourcefilestart(String SourceFileStart) {
        this.SourceFileStart = SourceFileStart;
    }
    public String getMidfile() {
        return MidFile;
    }

    public void setMidfile(String MidFile) {
        this.MidFile = MidFile;
    }


}