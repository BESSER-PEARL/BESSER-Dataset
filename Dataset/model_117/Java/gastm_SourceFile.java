





import java.util.List;
import java.util.ArrayList;

public class gastm_SourceFile extends GASTMSourceObject {

    private String path;





    private gastm_SourceLocation gastm_sourcelocation;




    private gastm_SourceFileReference gastm_sourcefilereference;


    public gastm_SourceFile(
        String path    ) {
        super(
        );
        this.path = path;
    }


    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }

    public gastm_SourceLocation getGastm_sourcelocation() {
        return gastm_sourcelocation;
    }

    public void setGastm_sourcelocation(gastm_SourceLocation gastm_sourcelocation) {
        this.gastm_sourcelocation = gastm_sourcelocation;
    }
    public gastm_SourceFileReference getGastm_sourcefilereference() {
        return gastm_sourcefilereference;
    }

    public void setGastm_sourcefilereference(gastm_SourceFileReference gastm_sourcefilereference) {
        this.gastm_sourcefilereference = gastm_sourcefilereference;
    }

}