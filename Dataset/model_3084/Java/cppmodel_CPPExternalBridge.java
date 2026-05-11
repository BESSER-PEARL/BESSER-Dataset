





import java.util.List;
import java.util.ArrayList;

public class cppmodel_CPPExternalBridge extends CPPQualifiedNamedElement {

    private String cppExternalNamespace;



    public cppmodel_CPPExternalBridge(
        String cppExternalNamespace    ) {
        super(
        );
        this.cppExternalNamespace = cppExternalNamespace;
    }


    public String getCppexternalnamespace() {
        return cppExternalNamespace;
    }

    public void setCppexternalnamespace(String cppExternalNamespace) {
        this.cppExternalNamespace = cppExternalNamespace;
    }


}