





import java.util.List;
import java.util.ArrayList;

public class express_core_EntityType extends core_NamedType, core_InstantiableType {

    private String isAbstract;





    private List<Attribute> attributes;




    private List<Role> roles;




    private SingleEntityType singleentitytype;




    private List<EntityType> entitytypes;




    private List<RangeRole> rangeroles;




    private List<InvertibleAttribute> invertibleattributes;




    private List<DomainRole> domainroles;




    private List<Extent> extents;




    private List<UniqueRule> uniquerules;




    private List<InvertibleAttribute> invertibleattributes;




    private List<Redeclaration> redeclarations;


    public express_core_EntityType(
        String isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.attributes = new ArrayList<>();
        this.roles = new ArrayList<>();
        this.entitytypes = new ArrayList<>();
        this.rangeroles = new ArrayList<>();
        this.invertibleattributes = new ArrayList<>();
        this.domainroles = new ArrayList<>();
        this.extents = new ArrayList<>();
        this.uniquerules = new ArrayList<>();
        this.invertibleattributes = new ArrayList<>();
        this.redeclarations = new ArrayList<>();
    }

    public express_core_EntityType(
        String isAbstract        ArrayList<Attribute> attributes,        ArrayList<Role> roles,        ArrayList<EntityType> entitytypes,        ArrayList<RangeRole> rangeroles,        ArrayList<InvertibleAttribute> invertibleattributes,        ArrayList<DomainRole> domainroles,        ArrayList<Extent> extents,        ArrayList<UniqueRule> uniquerules,        ArrayList<InvertibleAttribute> invertibleattributes,        ArrayList<Redeclaration> redeclarations    ) {
        this.isAbstract = isAbstract;
        this.attributes = attributes;
        this.roles = roles;
        this.entitytypes = entitytypes;
        this.rangeroles = rangeroles;
        this.invertibleattributes = invertibleattributes;
        this.domainroles = domainroles;
        this.extents = extents;
        this.uniquerules = uniquerules;
        this.invertibleattributes = invertibleattributes;
        this.redeclarations = redeclarations;
    }

    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
        this.isAbstract = isAbstract;
    }

    public List<Attribute> getAttributes() {
        return attributes;
    }

    public void addAttribute(Attribute attribute) {
        this.attributes.add(attribute);
    }
    public List<Role> getRoles() {
        return roles;
    }

    public void addRole(Role role) {
        this.roles.add(role);
    }
    public SingleEntityType getSingleentitytype() {
        return singleentitytype;
    }

    public void setSingleentitytype(SingleEntityType singleentitytype) {
        this.singleentitytype = singleentitytype;
    }
    public List<EntityType> getEntitytypes() {
        return entitytypes;
    }

    public void addEntitytype(Entitytype entitytype) {
        this.entitytypes.add(entitytype);
    }
    public List<RangeRole> getRangeroles() {
        return rangeroles;
    }

    public void addRangerole(Rangerole rangerole) {
        this.rangeroles.add(rangerole);
    }
    public List<InvertibleAttribute> getInvertibleattributes() {
        return invertibleattributes;
    }

    public void addInvertibleattribute(Invertibleattribute invertibleattribute) {
        this.invertibleattributes.add(invertibleattribute);
    }
    public List<DomainRole> getDomainroles() {
        return domainroles;
    }

    public void addDomainrole(Domainrole domainrole) {
        this.domainroles.add(domainrole);
    }
    public List<Extent> getExtents() {
        return extents;
    }

    public void addExtent(Extent extent) {
        this.extents.add(extent);
    }
    public List<UniqueRule> getUniquerules() {
        return uniquerules;
    }

    public void addUniquerule(Uniquerule uniquerule) {
        this.uniquerules.add(uniquerule);
    }
    public List<InvertibleAttribute> getInvertibleattributes() {
        return invertibleattributes;
    }

    public void addInvertibleattribute(Invertibleattribute invertibleattribute) {
        this.invertibleattributes.add(invertibleattribute);
    }
    public List<Redeclaration> getRedeclarations() {
        return redeclarations;
    }

    public void addRedeclaration(Redeclaration redeclaration) {
        this.redeclarations.add(redeclaration);
    }

}