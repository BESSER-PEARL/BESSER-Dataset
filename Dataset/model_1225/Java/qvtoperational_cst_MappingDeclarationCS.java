





import java.util.List;
import java.util.ArrayList;

public class qvtoperational_cst_MappingDeclarationCS extends CSTNode {

    private boolean isQuery;
    private String qualifiers;



    public qvtoperational_cst_MappingDeclarationCS(
        boolean isQuery,        String qualifiers    ) {
        super(
        );
        this.isQuery = isQuery;
        this.qualifiers = qualifiers;
    }


    public boolean getIsquery() {
        return isQuery;
    }

    public void setIsquery(boolean isQuery) {
        this.isQuery = isQuery;
    }
    public String getQualifiers() {
        return qualifiers;
    }

    public void setQualifiers(String qualifiers) {
        this.qualifiers = qualifiers;
    }


}