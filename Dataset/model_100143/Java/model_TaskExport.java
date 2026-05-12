





import java.util.List;
import java.util.ArrayList;

public class model_TaskExport extends Task {






    private model_IFile model_ifile;




    private List<model_MappingExport> model_mappingexports;




    private model_Table model_table;


    public model_TaskExport(
    ) {
        super(
        );
        this.model_mappingexports = new ArrayList<>();
    }

    public model_TaskExport(
        ArrayList<model_MappingExport> model_mappingexports    ) {
        this.model_mappingexports = model_mappingexports;
    }


    public model_IFile getModel_ifile() {
        return model_ifile;
    }

    public void setModel_ifile(model_IFile model_ifile) {
        this.model_ifile = model_ifile;
    }
    public List<model_MappingExport> getModel_mappingexports() {
        return model_mappingexports;
    }

    public void addModel_mappingexport(Model_mappingexport model_mappingexport) {
        this.model_mappingexports.add(model_mappingexport);
    }
    public model_Table getModel_table() {
        return model_table;
    }

    public void setModel_table(model_Table model_table) {
        this.model_table = model_table;
    }

}