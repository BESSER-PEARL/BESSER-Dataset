





import java.util.List;
import java.util.ArrayList;

public class qvtoperational_cst_ParameterDeclarationCS extends CSTNode {

    private String directionKind;



    public qvtoperational_cst_ParameterDeclarationCS(
        String directionKind    ) {
        super(
        );
        this.directionKind = directionKind;
    }


    public String getDirectionkind() {
        return directionKind;
    }

    public void setDirectionkind(String directionKind) {
        this.directionKind = directionKind;
    }


}