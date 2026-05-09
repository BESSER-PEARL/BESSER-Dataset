





import java.util.List;
import java.util.ArrayList;

public class JDTAST_TypeDeclaration extends AbstractTypeDeclaration {

    private String interface;





    private List<JDTAST_Type> jdtast_types;




    private List<JDTAST_TypeParameter> jdtast_typeparameters;




    private JDTAST_Type jdtast_type;


    public JDTAST_TypeDeclaration(
        String interface    ) {
        super(
        );
        this.interface = interface;
        this.jdtast_types = new ArrayList<>();
        this.jdtast_typeparameters = new ArrayList<>();
    }

    public JDTAST_TypeDeclaration(
        String interface        ArrayList<JDTAST_Type> jdtast_types,        ArrayList<JDTAST_TypeParameter> jdtast_typeparameters    ) {
        this.interface = interface;
        this.jdtast_types = jdtast_types;
        this.jdtast_typeparameters = jdtast_typeparameters;
    }

    public String getInterface() {
        return interface;
    }

    public void setInterface(String interface) {
        this.interface = interface;
    }

    public List<JDTAST_Type> getJdtast_types() {
        return jdtast_types;
    }

    public void addJdtast_type(Jdtast_type jdtast_type) {
        this.jdtast_types.add(jdtast_type);
    }
    public List<JDTAST_TypeParameter> getJdtast_typeparameters() {
        return jdtast_typeparameters;
    }

    public void addJdtast_typeparameter(Jdtast_typeparameter jdtast_typeparameter) {
        this.jdtast_typeparameters.add(jdtast_typeparameter);
    }
    public JDTAST_Type getJdtast_type() {
        return jdtast_type;
    }

    public void setJdtast_type(JDTAST_Type jdtast_type) {
        this.jdtast_type = jdtast_type;
    }

}