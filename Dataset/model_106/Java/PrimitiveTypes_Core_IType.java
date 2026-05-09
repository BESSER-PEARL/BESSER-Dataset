





import java.util.List;
import java.util.ArrayList;

public class PrimitiveTypes_Core_IType extends IMember {

    private String fullyQualifiedParametrizedName;
    private String fullyQualifiedName;





    private List<Core_ITypeParameter> core_itypeparameters;




    private List<Core_IInitializer> core_iinitializers;




    private List<Core_IType> core_itypes;




    private List<Core_IField> core_ifields;


    public PrimitiveTypes_Core_IType(
        String fullyQualifiedParametrizedName,        String fullyQualifiedName    ) {
        super(
        );
        this.fullyQualifiedParametrizedName = fullyQualifiedParametrizedName;
        this.fullyQualifiedName = fullyQualifiedName;
        this.core_itypeparameters = new ArrayList<>();
        this.core_iinitializers = new ArrayList<>();
        this.core_itypes = new ArrayList<>();
        this.core_ifields = new ArrayList<>();
    }

    public PrimitiveTypes_Core_IType(
        String fullyQualifiedParametrizedName,        String fullyQualifiedName        ArrayList<Core_ITypeParameter> core_itypeparameters,        ArrayList<Core_IInitializer> core_iinitializers,        ArrayList<Core_IType> core_itypes,        ArrayList<Core_IField> core_ifields    ) {
        this.fullyQualifiedParametrizedName = fullyQualifiedParametrizedName;
        this.fullyQualifiedName = fullyQualifiedName;
        this.core_itypeparameters = core_itypeparameters;
        this.core_iinitializers = core_iinitializers;
        this.core_itypes = core_itypes;
        this.core_ifields = core_ifields;
    }

    public String getFullyqualifiedparametrizedname() {
        return fullyQualifiedParametrizedName;
    }

    public void setFullyqualifiedparametrizedname(String fullyQualifiedParametrizedName) {
        this.fullyQualifiedParametrizedName = fullyQualifiedParametrizedName;
    }
    public String getFullyqualifiedname() {
        return fullyQualifiedName;
    }

    public void setFullyqualifiedname(String fullyQualifiedName) {
        this.fullyQualifiedName = fullyQualifiedName;
    }

    public List<Core_ITypeParameter> getCore_itypeparameters() {
        return core_itypeparameters;
    }

    public void addCore_itypeparameter(Core_itypeparameter core_itypeparameter) {
        this.core_itypeparameters.add(core_itypeparameter);
    }
    public List<Core_IInitializer> getCore_iinitializers() {
        return core_iinitializers;
    }

    public void addCore_iinitializer(Core_iinitializer core_iinitializer) {
        this.core_iinitializers.add(core_iinitializer);
    }
    public List<Core_IType> getCore_itypes() {
        return core_itypes;
    }

    public void addCore_itype(Core_itype core_itype) {
        this.core_itypes.add(core_itype);
    }
    public List<Core_IField> getCore_ifields() {
        return core_ifields;
    }

    public void addCore_ifield(Core_ifield core_ifield) {
        this.core_ifields.add(core_ifield);
    }

}