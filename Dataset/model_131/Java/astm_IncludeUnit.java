





import java.util.List;
import java.util.ArrayList;

public class astm_IncludeUnit extends PreprocessorElement {






    private astm_RDBIndexColumn astm_rdbindexcolumn;




    private astm_SourceFile astm_sourcefile;


    public astm_IncludeUnit(
    ) {
        super(
        );
    }



    public astm_RDBIndexColumn getAstm_rdbindexcolumn() {
        return astm_rdbindexcolumn;
    }

    public void setAstm_rdbindexcolumn(astm_RDBIndexColumn astm_rdbindexcolumn) {
        this.astm_rdbindexcolumn = astm_rdbindexcolumn;
    }
    public astm_SourceFile getAstm_sourcefile() {
        return astm_sourcefile;
    }

    public void setAstm_sourcefile(astm_SourceFile astm_sourcefile) {
        this.astm_sourcefile = astm_sourcefile;
    }

}