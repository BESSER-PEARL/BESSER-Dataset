





import java.util.List;
import java.util.ArrayList;

public class domainmodel_StatelessComponent extends BusinessFeatureType, AbstractNamespaceElement {

    private String name;



    public domainmodel_StatelessComponent(
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