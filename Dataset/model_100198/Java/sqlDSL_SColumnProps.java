





import java.util.List;
import java.util.ArrayList;

public class sqlDSL_SColumnProps  {

    private String javacolumn;
    private String index;
    private boolean nullable;
    private boolean aes;





    private sqlDSL_STableMember sqldsl_stablemember;


    public sqlDSL_SColumnProps(
        String javacolumn,        String index,        boolean nullable,        boolean aes    ) {
        this.javacolumn = javacolumn;
        this.index = index;
        this.nullable = nullable;
        this.aes = aes;
    }


    public String getJavacolumn() {
        return javacolumn;
    }

    public void setJavacolumn(String javacolumn) {
        this.javacolumn = javacolumn;
    }
    public String getIndex() {
        return index;
    }

    public void setIndex(String index) {
        this.index = index;
    }
    public boolean getNullable() {
        return nullable;
    }

    public void setNullable(boolean nullable) {
        this.nullable = nullable;
    }
    public boolean getAes() {
        return aes;
    }

    public void setAes(boolean aes) {
        this.aes = aes;
    }

    public sqlDSL_STableMember getSqldsl_stablemember() {
        return sqldsl_stablemember;
    }

    public void setSqldsl_stablemember(sqlDSL_STableMember sqldsl_stablemember) {
        this.sqldsl_stablemember = sqldsl_stablemember;
    }

}