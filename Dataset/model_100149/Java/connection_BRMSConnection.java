





import java.util.List;
import java.util.ArrayList;

public class connection_BRMSConnection extends Connection {

    private String urlName;
    private String tacWebappName;
    private String className;
    private String xmlField;
    private String moduleUsed;
    private String package;



    public connection_BRMSConnection(
        String urlName,        String tacWebappName,        String className,        String xmlField,        String moduleUsed,        String package    ) {
        super(
        );
        this.urlName = urlName;
        this.tacWebappName = tacWebappName;
        this.className = className;
        this.xmlField = xmlField;
        this.moduleUsed = moduleUsed;
        this.package = package;
    }


    public String getUrlname() {
        return urlName;
    }

    public void setUrlname(String urlName) {
        this.urlName = urlName;
    }
    public String getTacwebappname() {
        return tacWebappName;
    }

    public void setTacwebappname(String tacWebappName) {
        this.tacWebappName = tacWebappName;
    }
    public String getClassname() {
        return className;
    }

    public void setClassname(String className) {
        this.className = className;
    }
    public String getXmlfield() {
        return xmlField;
    }

    public void setXmlfield(String xmlField) {
        this.xmlField = xmlField;
    }
    public String getModuleused() {
        return moduleUsed;
    }

    public void setModuleused(String moduleUsed) {
        this.moduleUsed = moduleUsed;
    }
    public String getPackage() {
        return package;
    }

    public void setPackage(String package) {
        this.package = package;
    }


}