





import java.util.List;
import java.util.ArrayList;

public class dbl_StructuralSymbolReference extends NamedElement, PlainSymbolReference {

    private boolean list;
    private boolean globalScopedReference;
    private boolean composite;
    private boolean localScopedReference;



    public dbl_StructuralSymbolReference(
        boolean list,        boolean globalScopedReference,        boolean composite,        boolean localScopedReference    ) {
        super(
        );
        this.list = list;
        this.globalScopedReference = globalScopedReference;
        this.composite = composite;
        this.localScopedReference = localScopedReference;
    }


    public boolean getList() {
        return list;
    }

    public void setList(boolean list) {
        this.list = list;
    }
    public boolean getGlobalscopedreference() {
        return globalScopedReference;
    }

    public void setGlobalscopedreference(boolean globalScopedReference) {
        this.globalScopedReference = globalScopedReference;
    }
    public boolean getComposite() {
        return composite;
    }

    public void setComposite(boolean composite) {
        this.composite = composite;
    }
    public boolean getLocalscopedreference() {
        return localScopedReference;
    }

    public void setLocalscopedreference(boolean localScopedReference) {
        this.localScopedReference = localScopedReference;
    }


}