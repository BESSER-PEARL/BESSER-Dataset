





import java.util.List;
import java.util.ArrayList;

public class model_TaskFile extends Task {






    private model_File model_file;




    private model_File model_file;




    private List<model_MappingFile> model_mappingfiles;


    public model_TaskFile(
    ) {
        super(
        );
        this.model_mappingfiles = new ArrayList<>();
    }

    public model_TaskFile(
        ArrayList<model_MappingFile> model_mappingfiles    ) {
        this.model_mappingfiles = model_mappingfiles;
    }


    public model_File getModel_file() {
        return model_file;
    }

    public void setModel_file(model_File model_file) {
        this.model_file = model_file;
    }
    public model_File getModel_file() {
        return model_file;
    }

    public void setModel_file(model_File model_file) {
        this.model_file = model_file;
    }
    public List<model_MappingFile> getModel_mappingfiles() {
        return model_mappingfiles;
    }

    public void addModel_mappingfile(Model_mappingfile model_mappingfile) {
        this.model_mappingfiles.add(model_mappingfile);
    }

}