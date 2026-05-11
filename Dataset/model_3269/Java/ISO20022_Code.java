





import java.util.List;
import java.util.ArrayList;

public class ISO20022_Code extends RepositoryConcept {

    private String codeName;



    public ISO20022_Code(
        String codeName    ) {
        super(
        );
        this.codeName = codeName;
    }


    public String getCodename() {
        return codeName;
    }

    public void setCodename(String codeName) {
        this.codeName = codeName;
    }


}