





import java.util.List;
import java.util.ArrayList;

public class model_File extends IFile, SeparatedElement {

    private String numberOfHeaderLines;
    private String files;





    private List<model_Field> model_fields;


    public model_File(
        String numberOfHeaderLines,        String files    ) {
        super(
        );
        this.numberOfHeaderLines = numberOfHeaderLines;
        this.files = files;
        this.model_fields = new ArrayList<>();
    }

    public model_File(
        String numberOfHeaderLines,        String files        ArrayList<model_Field> model_fields    ) {
        this.numberOfHeaderLines = numberOfHeaderLines;
        this.files = files;
        this.model_fields = model_fields;
    }

    public String getNumberofheaderlines() {
        return numberOfHeaderLines;
    }

    public void setNumberofheaderlines(String numberOfHeaderLines) {
        this.numberOfHeaderLines = numberOfHeaderLines;
    }
    public String getFiles() {
        return files;
    }

    public void setFiles(String files) {
        this.files = files;
    }

    public List<model_Field> getModel_fields() {
        return model_fields;
    }

    public void addModel_field(Model_field model_field) {
        this.model_fields.add(model_field);
    }

}