





import java.util.List;
import java.util.ArrayList;

public class oracle_TableSpace extends ExtensibleModel {

    private String name;
    private String size;
    private String user;
    private String chineseName;
    private String description;
    private String file;
    private String logicName;





    private oracle_OracleSpaceResourceData oracle_oraclespaceresourcedata;


    public oracle_TableSpace(
        String name,        String size,        String user,        String chineseName,        String description,        String file,        String logicName    ) {
        super(
        );
        this.name = name;
        this.size = size;
        this.user = user;
        this.chineseName = chineseName;
        this.description = description;
        this.file = file;
        this.logicName = logicName;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }
    public String getUser() {
        return user;
    }

    public void setUser(String user) {
        this.user = user;
    }
    public String getChinesename() {
        return chineseName;
    }

    public void setChinesename(String chineseName) {
        this.chineseName = chineseName;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
    }
    public String getLogicname() {
        return logicName;
    }

    public void setLogicname(String logicName) {
        this.logicName = logicName;
    }

    public oracle_OracleSpaceResourceData getOracle_oraclespaceresourcedata() {
        return oracle_oraclespaceresourcedata;
    }

    public void setOracle_oraclespaceresourcedata(oracle_OracleSpaceResourceData oracle_oraclespaceresourcedata) {
        this.oracle_oraclespaceresourcedata = oracle_oraclespaceresourcedata;
    }

}