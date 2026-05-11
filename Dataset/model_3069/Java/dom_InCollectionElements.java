





import java.util.List;
import java.util.ArrayList;

public class dom_InCollectionElements extends FromRange {

    private String name;
    private String reference;



    public dom_InCollectionElements(
        String name,        String reference    ) {
        super(
        );
        this.name = name;
        this.reference = reference;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getReference() {
        return reference;
    }

    public void setReference(String reference) {
        this.reference = reference;
    }


}