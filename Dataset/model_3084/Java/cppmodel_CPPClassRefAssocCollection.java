





import java.util.List;
import java.util.ArrayList;

public class cppmodel_CPPClassRefAssocCollection extends OOPLClassRefAssocCollection, CPPQualifiedNamedElement {

    private String cppContainer;





    private cppmodel_CPPAttribute cppmodel_cppattribute;


    public cppmodel_CPPClassRefAssocCollection(
        String cppContainer    ) {
        super(
        );
        this.cppContainer = cppContainer;
    }


    public String getCppcontainer() {
        return cppContainer;
    }

    public void setCppcontainer(String cppContainer) {
        this.cppContainer = cppContainer;
    }

    public cppmodel_CPPAttribute getCppmodel_cppattribute() {
        return cppmodel_cppattribute;
    }

    public void setCppmodel_cppattribute(cppmodel_CPPAttribute cppmodel_cppattribute) {
        this.cppmodel_cppattribute = cppmodel_cppattribute;
    }

}