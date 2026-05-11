





import java.util.List;
import java.util.ArrayList;

public class cobol_sections_FileSection extends DataDivisionSection {






    private List<FileName> filenames;


    public cobol_sections_FileSection(
    ) {
        super(
        );
        this.filenames = new ArrayList<>();
    }

    public cobol_sections_FileSection(
        ArrayList<FileName> filenames    ) {
        this.filenames = filenames;
    }


    public List<FileName> getFilenames() {
        return filenames;
    }

    public void addFilename(Filename filename) {
        this.filenames.add(filename);
    }

}