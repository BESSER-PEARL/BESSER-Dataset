





import java.util.List;
import java.util.ArrayList;

public class UseCases_UseCase extends Classifier {

    private String extensionPoint;



    public UseCases_UseCase(
        String extensionPoint    ) {
        super(
        );
        this.extensionPoint = extensionPoint;
    }


    public String getExtensionpoint() {
        return extensionPoint;
    }

    public void setExtensionpoint(String extensionPoint) {
        this.extensionPoint = extensionPoint;
    }


}