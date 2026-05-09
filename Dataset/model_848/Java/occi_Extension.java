





import java.util.List;
import java.util.ArrayList;

public class occi_Extension  {

    private String description;
    private String scheme;
    private String name;
    private String specification;





    private List<occi_Extension> occi_extensions;




    private List<occi_DataType> occi_datatypes;




    private List<occi_Mixin> occi_mixins;




    private List<occi_Kind> occi_kinds;


    public occi_Extension(
        String description,        String scheme,        String name,        String specification    ) {
        this.description = description;
        this.scheme = scheme;
        this.name = name;
        this.specification = specification;
        this.occi_extensions = new ArrayList<>();
        this.occi_datatypes = new ArrayList<>();
        this.occi_mixins = new ArrayList<>();
        this.occi_kinds = new ArrayList<>();
    }

    public occi_Extension(
        String description,        String scheme,        String name,        String specification        ArrayList<occi_Extension> occi_extensions,        ArrayList<occi_DataType> occi_datatypes,        ArrayList<occi_Mixin> occi_mixins,        ArrayList<occi_Kind> occi_kinds    ) {
        this.description = description;
        this.scheme = scheme;
        this.name = name;
        this.specification = specification;
        this.occi_extensions = occi_extensions;
        this.occi_datatypes = occi_datatypes;
        this.occi_mixins = occi_mixins;
        this.occi_kinds = occi_kinds;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getScheme() {
        return scheme;
    }

    public void setScheme(String scheme) {
        this.scheme = scheme;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSpecification() {
        return specification;
    }

    public void setSpecification(String specification) {
        this.specification = specification;
    }

    public List<occi_Extension> getOcci_extensions() {
        return occi_extensions;
    }

    public void addOcci_extension(Occi_extension occi_extension) {
        this.occi_extensions.add(occi_extension);
    }
    public List<occi_DataType> getOcci_datatypes() {
        return occi_datatypes;
    }

    public void addOcci_datatype(Occi_datatype occi_datatype) {
        this.occi_datatypes.add(occi_datatype);
    }
    public List<occi_Mixin> getOcci_mixins() {
        return occi_mixins;
    }

    public void addOcci_mixin(Occi_mixin occi_mixin) {
        this.occi_mixins.add(occi_mixin);
    }
    public List<occi_Kind> getOcci_kinds() {
        return occi_kinds;
    }

    public void addOcci_kind(Occi_kind occi_kind) {
        this.occi_kinds.add(occi_kind);
    }

}