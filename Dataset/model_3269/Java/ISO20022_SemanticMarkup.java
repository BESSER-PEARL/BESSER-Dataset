





import java.util.List;
import java.util.ArrayList;

public class ISO20022_SemanticMarkup extends ModelEntity {

    private String type;





    private ISO20022_RepositoryConcept iso20022_repositoryconcept;


    public ISO20022_SemanticMarkup(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public ISO20022_RepositoryConcept getIso20022_repositoryconcept() {
        return iso20022_repositoryconcept;
    }

    public void setIso20022_repositoryconcept(ISO20022_RepositoryConcept iso20022_repositoryconcept) {
        this.iso20022_repositoryconcept = iso20022_repositoryconcept;
    }

}