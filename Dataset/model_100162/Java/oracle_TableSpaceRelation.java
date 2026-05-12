





import java.util.List;
import java.util.ArrayList;

public class oracle_TableSpaceRelation extends ExtensibleModel {

    private String indexSpace;
    private String mainSpace;





    private oracle_OracleSpaceResourceData oracle_oraclespaceresourcedata;


    public oracle_TableSpaceRelation(
        String indexSpace,        String mainSpace    ) {
        super(
        );
        this.indexSpace = indexSpace;
        this.mainSpace = mainSpace;
    }


    public String getIndexspace() {
        return indexSpace;
    }

    public void setIndexspace(String indexSpace) {
        this.indexSpace = indexSpace;
    }
    public String getMainspace() {
        return mainSpace;
    }

    public void setMainspace(String mainSpace) {
        this.mainSpace = mainSpace;
    }

    public oracle_OracleSpaceResourceData getOracle_oraclespaceresourcedata() {
        return oracle_oraclespaceresourcedata;
    }

    public void setOracle_oraclespaceresourcedata(oracle_OracleSpaceResourceData oracle_oraclespaceresourcedata) {
        this.oracle_oraclespaceresourcedata = oracle_oraclespaceresourcedata;
    }

}