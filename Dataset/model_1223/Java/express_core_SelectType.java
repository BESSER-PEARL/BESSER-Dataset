





import java.util.List;
import java.util.ArrayList;

public class express_core_SelectType extends DefinedType {

    private String isExtensible;
    private String isEntity;





    private List<NamedType> namedtypes;




    private List<NamedType> namedtypes;


    public express_core_SelectType(
        String isExtensible,        String isEntity    ) {
        super(
        );
        this.isExtensible = isExtensible;
        this.isEntity = isEntity;
        this.namedtypes = new ArrayList<>();
        this.namedtypes = new ArrayList<>();
    }

    public express_core_SelectType(
        String isExtensible,        String isEntity        ArrayList<NamedType> namedtypes,        ArrayList<NamedType> namedtypes    ) {
        this.isExtensible = isExtensible;
        this.isEntity = isEntity;
        this.namedtypes = namedtypes;
        this.namedtypes = namedtypes;
    }

    public String getIsextensible() {
        return isExtensible;
    }

    public void setIsextensible(String isExtensible) {
        this.isExtensible = isExtensible;
    }
    public String getIsentity() {
        return isEntity;
    }

    public void setIsentity(String isEntity) {
        this.isEntity = isEntity;
    }

    public List<NamedType> getNamedtypes() {
        return namedtypes;
    }

    public void addNamedtype(Namedtype namedtype) {
        this.namedtypes.add(namedtype);
    }
    public List<NamedType> getNamedtypes() {
        return namedtypes;
    }

    public void addNamedtype(Namedtype namedtype) {
        this.namedtypes.add(namedtype);
    }

}