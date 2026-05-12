





import java.util.List;
import java.util.ArrayList;

public class DatadiagramMLXForm_VisioDocument  {

    private String start;
    private String key;
    private String buildnum;
    private String metric;
    private String version;
    private String docLangId;





    private ColorsTable colorstable;




    private DocumentSettingsElt documentsettingselt;




    private PrintSetup printsetup;




    private FontsTable fontstable;




    private FaceNamesTable facenamestable;


    public DatadiagramMLXForm_VisioDocument(
        String start,        String key,        String buildnum,        String metric,        String version,        String docLangId    ) {
        this.start = start;
        this.key = key;
        this.buildnum = buildnum;
        this.metric = metric;
        this.version = version;
        this.docLangId = docLangId;
    }


    public String getStart() {
        return start;
    }

    public void setStart(String start) {
        this.start = start;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getBuildnum() {
        return buildnum;
    }

    public void setBuildnum(String buildnum) {
        this.buildnum = buildnum;
    }
    public String getMetric() {
        return metric;
    }

    public void setMetric(String metric) {
        this.metric = metric;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getDoclangid() {
        return docLangId;
    }

    public void setDoclangid(String docLangId) {
        this.docLangId = docLangId;
    }

    public ColorsTable getColorstable() {
        return colorstable;
    }

    public void setColorstable(ColorsTable colorstable) {
        this.colorstable = colorstable;
    }
    public DocumentSettingsElt getDocumentsettingselt() {
        return documentsettingselt;
    }

    public void setDocumentsettingselt(DocumentSettingsElt documentsettingselt) {
        this.documentsettingselt = documentsettingselt;
    }
    public PrintSetup getPrintsetup() {
        return printsetup;
    }

    public void setPrintsetup(PrintSetup printsetup) {
        this.printsetup = printsetup;
    }
    public FontsTable getFontstable() {
        return fontstable;
    }

    public void setFontstable(FontsTable fontstable) {
        this.fontstable = fontstable;
    }
    public FaceNamesTable getFacenamestable() {
        return facenamestable;
    }

    public void setFacenamestable(FaceNamesTable facenamestable) {
        this.facenamestable = facenamestable;
    }

}