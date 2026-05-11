





import java.util.List;
import java.util.ArrayList;

public class logiclanguage_Type extends TypeDescriptor {

    private boolean isAbstract;
    private String name;





    private List<logiclanguage_Type> logiclanguage_types;




    private logiclanguage_ComplexTypeReference logiclanguage_complextypereference;




    private logiclanguage_Type logiclanguage_type;


    public logiclanguage_Type(
        boolean isAbstract,        String name    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.name = name;
        this.logiclanguage_types = new ArrayList<>();
    }

    public logiclanguage_Type(
        boolean isAbstract,        String name        ArrayList<logiclanguage_Type> logiclanguage_types    ) {
        this.isAbstract = isAbstract;
        this.name = name;
        this.logiclanguage_types = logiclanguage_types;
    }

    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<logiclanguage_Type> getLogiclanguage_types() {
        return logiclanguage_types;
    }

    public void addLogiclanguage_type(Logiclanguage_type logiclanguage_type) {
        this.logiclanguage_types.add(logiclanguage_type);
    }
    public logiclanguage_ComplexTypeReference getLogiclanguage_complextypereference() {
        return logiclanguage_complextypereference;
    }

    public void setLogiclanguage_complextypereference(logiclanguage_ComplexTypeReference logiclanguage_complextypereference) {
        this.logiclanguage_complextypereference = logiclanguage_complextypereference;
    }
    public logiclanguage_Type getLogiclanguage_type() {
        return logiclanguage_type;
    }

    public void setLogiclanguage_type(logiclanguage_Type logiclanguage_type) {
        this.logiclanguage_type = logiclanguage_type;
    }

}