





import java.util.List;
import java.util.ArrayList;

public class connection_BRMSConnection extends Connection {

    private String moduleUsed;
    private String package;
    private String xmlField;
    private String urlName;
    private String className;
    private String tacWebappName;





    private List<connection_XMLFileNode> connection_xmlfilenodes;




    private List<connection_XMLFileNode> connection_xmlfilenodes;




    private List<connection_XMLFileNode> connection_xmlfilenodes;


    public connection_BRMSConnection(
        String moduleUsed,        String package,        String xmlField,        String urlName,        String className,        String tacWebappName    ) {
        super(
        );
        this.moduleUsed = moduleUsed;
        this.package = package;
        this.xmlField = xmlField;
        this.urlName = urlName;
        this.className = className;
        this.tacWebappName = tacWebappName;
        this.connection_xmlfilenodes = new ArrayList<>();
        this.connection_xmlfilenodes = new ArrayList<>();
        this.connection_xmlfilenodes = new ArrayList<>();
    }

    public connection_BRMSConnection(
        String moduleUsed,        String package,        String xmlField,        String urlName,        String className,        String tacWebappName        ArrayList<connection_XMLFileNode> connection_xmlfilenodes,        ArrayList<connection_XMLFileNode> connection_xmlfilenodes,        ArrayList<connection_XMLFileNode> connection_xmlfilenodes    ) {
        this.moduleUsed = moduleUsed;
        this.package = package;
        this.xmlField = xmlField;
        this.urlName = urlName;
        this.className = className;
        this.tacWebappName = tacWebappName;
        this.connection_xmlfilenodes = connection_xmlfilenodes;
        this.connection_xmlfilenodes = connection_xmlfilenodes;
        this.connection_xmlfilenodes = connection_xmlfilenodes;
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
    public String getXmlfield() {
        return xmlField;
    }

    public void setXmlfield(String xmlField) {
        this.xmlField = xmlField;
    }
    public String getUrlname() {
        return urlName;
    }

    public void setUrlname(String urlName) {
        this.urlName = urlName;
    }
    public String getClassname() {
        return className;
    }

    public void setClassname(String className) {
        this.className = className;
    }
    public String getTacwebappname() {
        return tacWebappName;
    }

    public void setTacwebappname(String tacWebappName) {
        this.tacWebappName = tacWebappName;
    }

    public List<connection_XMLFileNode> getConnection_xmlfilenodes() {
        return connection_xmlfilenodes;
    }

    public void addConnection_xmlfilenode(Connection_xmlfilenode connection_xmlfilenode) {
        this.connection_xmlfilenodes.add(connection_xmlfilenode);
    }
    public List<connection_XMLFileNode> getConnection_xmlfilenodes() {
        return connection_xmlfilenodes;
    }

    public void addConnection_xmlfilenode(Connection_xmlfilenode connection_xmlfilenode) {
        this.connection_xmlfilenodes.add(connection_xmlfilenode);
    }
    public List<connection_XMLFileNode> getConnection_xmlfilenodes() {
        return connection_xmlfilenodes;
    }

    public void addConnection_xmlfilenode(Connection_xmlfilenode connection_xmlfilenode) {
        this.connection_xmlfilenodes.add(connection_xmlfilenode);
    }

}