





import java.util.List;
import java.util.ArrayList;

public class domainmodel_InterfaceDeclaration extends BusinessFeatureType, AbstractNamespaceElement {

    private String name;



    public domainmodel_InterfaceDeclaration(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}