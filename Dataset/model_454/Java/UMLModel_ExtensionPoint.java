





import java.util.List;
import java.util.ArrayList;

public class UMLModel_ExtensionPoint extends RedefinableElement {

    private String useCase;



    public UMLModel_ExtensionPoint(
        String useCase    ) {
        super(
        );
        this.useCase = useCase;
    }


    public String getUsecase() {
        return useCase;
    }

    public void setUsecase(String useCase) {
        this.useCase = useCase;
    }


}