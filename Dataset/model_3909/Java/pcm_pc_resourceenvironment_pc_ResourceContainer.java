





import java.util.List;
import java.util.ArrayList;

public class pcm_pc_resourceenvironment_pc_ResourceContainer extends Entity {






    private List<ProcessingResourceSpecification> processingresourcespecifications;


    public pcm_pc_resourceenvironment_pc_ResourceContainer(
    ) {
        super(
        );
        this.processingresourcespecifications = new ArrayList<>();
    }

    public pcm_pc_resourceenvironment_pc_ResourceContainer(
        ArrayList<ProcessingResourceSpecification> processingresourcespecifications    ) {
        this.processingresourcespecifications = processingresourcespecifications;
    }


    public List<ProcessingResourceSpecification> getProcessingresourcespecifications() {
        return processingresourcespecifications;
    }

    public void addProcessingresourcespecification(Processingresourcespecification processingresourcespecification) {
        this.processingresourcespecifications.add(processingresourcespecification);
    }

}