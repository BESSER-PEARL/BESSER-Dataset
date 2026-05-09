





import java.util.List;
import java.util.ArrayList;

public class rif11a_ExchangeFile_DatatypeDefinitionBinaryFile extends DatatypeDefinitionComplex {

    private String filenameSuffix;
    private String formatName;
    private String application;
    private String mimeType;



    public rif11a_ExchangeFile_DatatypeDefinitionBinaryFile(
        String filenameSuffix,        String formatName,        String application,        String mimeType    ) {
        super(
        );
        this.filenameSuffix = filenameSuffix;
        this.formatName = formatName;
        this.application = application;
        this.mimeType = mimeType;
    }


    public String getFilenamesuffix() {
        return filenameSuffix;
    }

    public void setFilenamesuffix(String filenameSuffix) {
        this.filenameSuffix = filenameSuffix;
    }
    public String getFormatname() {
        return formatName;
    }

    public void setFormatname(String formatName) {
        this.formatName = formatName;
    }
    public String getApplication() {
        return application;
    }

    public void setApplication(String application) {
        this.application = application;
    }
    public String getMimetype() {
        return mimeType;
    }

    public void setMimetype(String mimeType) {
        this.mimeType = mimeType;
    }


}