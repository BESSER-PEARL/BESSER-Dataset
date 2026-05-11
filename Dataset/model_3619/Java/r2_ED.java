





import java.util.List;
import java.util.ArrayList;

public class r2_ED extends ANY {

    private String value;
    private String mediaType;
    private String data;
    private String charset;
    private String compression;
    private String integrityCheckAlgorithm;
    private String integrityCheck;
    private String language;





    private r2_TEL r2_tel;


    public r2_ED(
        String value,        String mediaType,        String data,        String charset,        String compression,        String integrityCheckAlgorithm,        String integrityCheck,        String language    ) {
        super(
        );
        this.value = value;
        this.mediaType = mediaType;
        this.data = data;
        this.charset = charset;
        this.compression = compression;
        this.integrityCheckAlgorithm = integrityCheckAlgorithm;
        this.integrityCheck = integrityCheck;
        this.language = language;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getMediatype() {
        return mediaType;
    }

    public void setMediatype(String mediaType) {
        this.mediaType = mediaType;
    }
    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }
    public String getCharset() {
        return charset;
    }

    public void setCharset(String charset) {
        this.charset = charset;
    }
    public String getCompression() {
        return compression;
    }

    public void setCompression(String compression) {
        this.compression = compression;
    }
    public String getIntegritycheckalgorithm() {
        return integrityCheckAlgorithm;
    }

    public void setIntegritycheckalgorithm(String integrityCheckAlgorithm) {
        this.integrityCheckAlgorithm = integrityCheckAlgorithm;
    }
    public String getIntegritycheck() {
        return integrityCheck;
    }

    public void setIntegritycheck(String integrityCheck) {
        this.integrityCheck = integrityCheck;
    }
    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }

    public r2_TEL getR2_tel() {
        return r2_tel;
    }

    public void setR2_tel(r2_TEL r2_tel) {
        this.r2_tel = r2_tel;
    }

}