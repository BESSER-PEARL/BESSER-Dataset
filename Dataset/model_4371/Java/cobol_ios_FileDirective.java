





import java.util.List;
import java.util.ArrayList;

public class cobol_ios_FileDirective extends IODirectives {






    private List<FileNameReference> filenamereferences;


    public cobol_ios_FileDirective(
    ) {
        super(
        );
        this.filenamereferences = new ArrayList<>();
    }

    public cobol_ios_FileDirective(
        ArrayList<FileNameReference> filenamereferences    ) {
        this.filenamereferences = filenamereferences;
    }


    public List<FileNameReference> getFilenamereferences() {
        return filenamereferences;
    }

    public void addFilenamereference(Filenamereference filenamereference) {
        this.filenamereferences.add(filenamereference);
    }

}