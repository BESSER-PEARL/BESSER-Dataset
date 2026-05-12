





import java.util.List;
import java.util.ArrayList;

public class connection_EDIFACTConnection extends Connection {

    private String XmlPath;
    private String FileName;
    private String XmlName;



    public connection_EDIFACTConnection(
        String XmlPath,        String FileName,        String XmlName    ) {
        super(
        );
        this.XmlPath = XmlPath;
        this.FileName = FileName;
        this.XmlName = XmlName;
    }


    public String getXmlpath() {
        return XmlPath;
    }

    public void setXmlpath(String XmlPath) {
        this.XmlPath = XmlPath;
    }
    public String getFilename() {
        return FileName;
    }

    public void setFilename(String FileName) {
        this.FileName = FileName;
    }
    public String getXmlname() {
        return XmlName;
    }

    public void setXmlname(String XmlName) {
        this.XmlName = XmlName;
    }


}