





import java.util.List;
import java.util.ArrayList;

public class gastm_VariableDeclaration extends Declaration {

    private String isMutable;



    public gastm_VariableDeclaration(
        String isMutable    ) {
        super(
        );
        this.isMutable = isMutable;
    }


    public String getIsmutable() {
        return isMutable;
    }

    public void setIsmutable(String isMutable) {
        this.isMutable = isMutable;
    }


}