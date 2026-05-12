





import java.util.List;
import java.util.ArrayList;

public class model_SCTFile extends IFile {

    private String file;





    private List<model_Domain> model_domains;




    private List<model_Column> model_columns;


    public model_SCTFile(
        String file    ) {
        super(
        );
        this.file = file;
        this.model_domains = new ArrayList<>();
        this.model_columns = new ArrayList<>();
    }

    public model_SCTFile(
        String file        ArrayList<model_Domain> model_domains,        ArrayList<model_Column> model_columns    ) {
        this.file = file;
        this.model_domains = model_domains;
        this.model_columns = model_columns;
    }

    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
    }

    public List<model_Domain> getModel_domains() {
        return model_domains;
    }

    public void addModel_domain(Model_domain model_domain) {
        this.model_domains.add(model_domain);
    }
    public List<model_Column> getModel_columns() {
        return model_columns;
    }

    public void addModel_column(Model_column model_column) {
        this.model_columns.add(model_column);
    }

}