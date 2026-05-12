





import java.util.List;
import java.util.ArrayList;

public class connection_EDIFACTConnection extends Connection {

    private String XmlName;
    private String FileName;
    private String XmlPath;



    public connection_EDIFACTConnection(
        String XmlName,        String FileName,        String XmlPath    ) {
        super(
        );
        this.XmlName = XmlName;
        this.FileName = FileName;
        this.XmlPath = XmlPath;
    }


    public String getXmlname() {
        return XmlName;
    }

    public void setXmlname(String XmlName) {
        this.XmlName = XmlName;
    }
    public String getFilename() {
        return FileName;
    }

    public void setFilename(String FileName) {
        this.FileName = FileName;
    }
    public String getXmlpath() {
        return XmlPath;
    }

    public void setXmlpath(String XmlPath) {
        this.XmlPath = XmlPath;
    }


}