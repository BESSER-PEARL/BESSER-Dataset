





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedPackageImport extends TracedDirectedRelationship {






    private uml_TracedNamespace uml_tracednamespace;




    private uml_TracedPackage uml_tracedpackage;


    public umlTrace_uml_TracedPackageImport(
    ) {
        super(
        );
    }



    public uml_TracedNamespace getUml_tracednamespace() {
        return uml_tracednamespace;
    }

    public void setUml_tracednamespace(uml_TracedNamespace uml_tracednamespace) {
        this.uml_tracednamespace = uml_tracednamespace;
    }
    public uml_TracedPackage getUml_tracedpackage() {
        return uml_tracedpackage;
    }

    public void setUml_tracedpackage(uml_TracedPackage uml_tracedpackage) {
        this.uml_tracedpackage = uml_tracedpackage;
    }

}