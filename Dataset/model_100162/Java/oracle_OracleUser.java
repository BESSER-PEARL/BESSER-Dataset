





import java.util.List;
import java.util.ArrayList;

public class oracle_OracleUser extends ExtensibleModel {

    private String attributes;
    private String password;
    private String decription;
    private String name;
    private String defaultTableSpace;
    private boolean enable;





    private oracle_OracleUserResourceData oracle_oracleuserresourcedata;


    public oracle_OracleUser(
        String attributes,        String password,        String decription,        String name,        String defaultTableSpace,        boolean enable    ) {
        super(
        );
        this.attributes = attributes;
        this.password = password;
        this.decription = decription;
        this.name = name;
        this.defaultTableSpace = defaultTableSpace;
        this.enable = enable;
    }


    public String getAttributes() {
        return attributes;
    }

    public void setAttributes(String attributes) {
        this.attributes = attributes;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getDecription() {
        return decription;
    }

    public void setDecription(String decription) {
        this.decription = decription;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDefaulttablespace() {
        return defaultTableSpace;
    }

    public void setDefaulttablespace(String defaultTableSpace) {
        this.defaultTableSpace = defaultTableSpace;
    }
    public boolean getEnable() {
        return enable;
    }

    public void setEnable(boolean enable) {
        this.enable = enable;
    }

    public oracle_OracleUserResourceData getOracle_oracleuserresourcedata() {
        return oracle_oracleuserresourcedata;
    }

    public void setOracle_oracleuserresourcedata(oracle_OracleUserResourceData oracle_oracleuserresourcedata) {
        this.oracle_oracleuserresourcedata = oracle_oracleuserresourcedata;
    }

}