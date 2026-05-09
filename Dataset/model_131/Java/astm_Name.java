





import java.util.List;
import java.util.ArrayList;

public class astm_Name extends OtherSyntaxObject {

    private String nameString;





    private astm_RDBIndex astm_rdbindex;


    public astm_Name(
        String nameString    ) {
        super(
        );
        this.nameString = nameString;
    }


    public String getNamestring() {
        return nameString;
    }

    public void setNamestring(String nameString) {
        this.nameString = nameString;
    }

    public astm_RDBIndex getAstm_rdbindex() {
        return astm_rdbindex;
    }

    public void setAstm_rdbindex(astm_RDBIndex astm_rdbindex) {
        this.astm_rdbindex = astm_rdbindex;
    }

}