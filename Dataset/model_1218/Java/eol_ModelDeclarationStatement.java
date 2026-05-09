





import java.util.List;
import java.util.ArrayList;

public class eol_ModelDeclarationStatement extends Statement {

    private String resolvedIMetamodel;



    public eol_ModelDeclarationStatement(
        String resolvedIMetamodel    ) {
        super(
        );
        this.resolvedIMetamodel = resolvedIMetamodel;
    }


    public String getResolvedimetamodel() {
        return resolvedIMetamodel;
    }

    public void setResolvedimetamodel(String resolvedIMetamodel) {
        this.resolvedIMetamodel = resolvedIMetamodel;
    }


}