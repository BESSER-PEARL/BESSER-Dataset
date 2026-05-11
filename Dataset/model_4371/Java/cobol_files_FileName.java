





import java.util.List;
import java.util.ArrayList;

public class cobol_files_FileName extends water_IncompleteElement, references_ReferenceableElement {

    private String fileDescriptor;



    public cobol_files_FileName(
        String fileDescriptor    ) {
        super(
        );
        this.fileDescriptor = fileDescriptor;
    }


    public String getFiledescriptor() {
        return fileDescriptor;
    }

    public void setFiledescriptor(String fileDescriptor) {
        this.fileDescriptor = fileDescriptor;
    }


}