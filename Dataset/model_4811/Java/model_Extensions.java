





import java.util.List;
import java.util.ArrayList;

public class model_Extensions extends BPELExtensibleElement {






    private model_Process model_process;




    private List<model_Extension> model_extensions;


    public model_Extensions(
    ) {
        super(
        );
        this.model_extensions = new ArrayList<>();
    }

    public model_Extensions(
        ArrayList<model_Extension> model_extensions    ) {
        this.model_extensions = model_extensions;
    }


    public model_Process getModel_process() {
        return model_process;
    }

    public void setModel_process(model_Process model_process) {
        this.model_process = model_process;
    }
    public List<model_Extension> getModel_extensions() {
        return model_extensions;
    }

    public void addModel_extension(Model_extension model_extension) {
        this.model_extensions.add(model_extension);
    }

}