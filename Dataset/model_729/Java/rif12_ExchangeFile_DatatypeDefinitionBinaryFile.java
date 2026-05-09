





import java.util.List;
import java.util.ArrayList;

public class rif12_ExchangeFile_DatatypeDefinitionBinaryFile extends DatatypeDefinitionComplex {

    private String application;
    private String mimeType;
    private String filenameSuffix;
    private String formatName;



    public rif12_ExchangeFile_DatatypeDefinitionBinaryFile(
        String application,        String mimeType,        String filenameSuffix,        String formatName    ) {
        super(
        );
        this.application = application;
        this.mimeType = mimeType;
        this.filenameSuffix = filenameSuffix;
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


}