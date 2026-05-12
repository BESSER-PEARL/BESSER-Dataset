





import java.util.List;
import java.util.ArrayList;

public class model_TaskImport extends Task {






    private List<model_MappingImport> model_mappingimports;




    private model_IFile model_ifile;




    private model_Table model_table;


    public model_TaskImport(
    ) {
        super(
        );
        this.model_mappingimports = new ArrayList<>();
    }

    public model_TaskImport(
        ArrayList<model_MappingImport> model_mappingimports    ) {
        this.model_mappingimports = model_mappingimports;
    }


    public List<model_MappingImport> getModel_mappingimports() {
        return model_mappingimports;
    }

    public void addModel_mappingimport(Model_mappingimport model_mappingimport) {
        this.model_mappingimports.add(model_mappingimport);
    }
    public model_IFile getModel_ifile() {
        return model_ifile;
    }

    public void setModel_ifile(model_IFile model_ifile) {
        this.model_ifile = model_ifile;
    }
    public model_Table getModel_table() {
        return model_table;
    }

    public void setModel_table(model_Table model_table) {
        this.model_table = model_table;
    }

}