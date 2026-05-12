





import java.util.List;
import java.util.ArrayList;

public class oracle_OraclePrivilege extends ExtensibleModel {

    private String name;
    private String type;
    private String decription;





    private oracle_OracleUserResourceData oracle_oracleuserresourcedata;




    private oracle_OracleUser oracle_oracleuser;


    public oracle_OraclePrivilege(
        String name,        String type,        String decription    ) {
        super(
        );
        this.name = name;
        this.type = type;
        this.decription = decription;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getDecription() {
        return decription;
    }

    public void setDecription(String decription) {
        this.decription = decription;
    }

    public oracle_OracleUserResourceData getOracle_oracleuserresourcedata() {
        return oracle_oracleuserresourcedata;
    }

    public void setOracle_oracleuserresourcedata(oracle_OracleUserResourceData oracle_oracleuserresourcedata) {
        this.oracle_oracleuserresourcedata = oracle_oracleuserresourcedata;
    }
    public oracle_OracleUser getOracle_oracleuser() {
        return oracle_oracleuser;
    }

    public void setOracle_oracleuser(oracle_OracleUser oracle_oracleuser) {
        this.oracle_oracleuser = oracle_oracleuser;
    }

}