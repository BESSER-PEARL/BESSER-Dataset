





import java.util.List;
import java.util.ArrayList;

public class astm_SourceFile extends GASTMSourceObject {

    private String pathName;





    private astm_SourceLocation astm_sourcelocation;


    public astm_SourceFile(
        String pathName    ) {
        super(
        );
        this.pathName = pathName;
    }


    public String getPathname() {
        return pathName;
    }

    public void setPathname(String pathName) {
        this.pathName = pathName;
    }

    public astm_SourceLocation getAstm_sourcelocation() {
        return astm_sourcelocation;
    }

    public void setAstm_sourcelocation(astm_SourceLocation astm_sourcelocation) {
        this.astm_sourcelocation = astm_sourcelocation;
    }

}