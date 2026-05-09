





import java.util.List;
import java.util.ArrayList;

public class qvtoperational_cst_MappingDeclarationCS extends CSTNode {

    private String qualifiers;
    private boolean isQuery;



    public qvtoperational_cst_MappingDeclarationCS(
        String qualifiers,        boolean isQuery    ) {
        super(
        );
        this.qualifiers = qualifiers;
        this.isQuery = isQuery;
    }


    public String getQualifiers() {
        return qualifiers;
    }

    public void setQualifiers(String qualifiers) {
        this.qualifiers = qualifiers;
    }
    public boolean getIsquery() {
        return isQuery;
    }

    public void setIsquery(boolean isQuery) {
        this.isQuery = isQuery;
    }


}