





import java.util.List;
import java.util.ArrayList;

public class model_Import extends BPELExtensibleElement {

    private String location;
    private String namespace;
    private String importType;





    private model_Process model_process;


    public model_Import(
        String location,        String namespace,        String importType    ) {
        super(
        );
        this.location = location;
        this.namespace = namespace;
        this.importType = importType;
    }


    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getNamespace() {
        return namespace;
    }

    public void setNamespace(String namespace) {
        this.namespace = namespace;
    }
    public String getImporttype() {
        return importType;
    }

    public void setImporttype(String importType) {
        this.importType = importType;
    }

    public model_Process getModel_process() {
        return model_process;
    }

    public void setModel_process(model_Process model_process) {
        this.model_process = model_process;
    }

}