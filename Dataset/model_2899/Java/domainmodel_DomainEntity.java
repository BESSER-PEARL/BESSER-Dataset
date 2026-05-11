





import java.util.List;
import java.util.ArrayList;

public class domainmodel_DomainEntity extends Type, AbstractNamespaceElement {

    private String name;



    public domainmodel_DomainEntity(
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