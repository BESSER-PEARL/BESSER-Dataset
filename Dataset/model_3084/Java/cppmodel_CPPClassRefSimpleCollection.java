





import java.util.List;
import java.util.ArrayList;

public class cppmodel_CPPClassRefSimpleCollection extends OOPLClassRefSimpleCollection, CPPQualifiedNamedElement {

    private String cppContainer;



    public cppmodel_CPPClassRefSimpleCollection(
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


}