





import java.util.List;
import java.util.ArrayList;

public class pcm_av_resourceenvironment_av_ResourceContainer extends Entity {






    private List<ProcessingResourceSpecification> processingresourcespecifications;


    public pcm_av_resourceenvironment_av_ResourceContainer(
    ) {
        super(
        );
        this.processingresourcespecifications = new ArrayList<>();
    }

    public pcm_av_resourceenvironment_av_ResourceContainer(
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