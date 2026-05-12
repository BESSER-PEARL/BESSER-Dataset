





import java.util.List;
import java.util.ArrayList;

public class dbmodel_Attribute  {

    private String descr;
    private String name;
    private boolean kukoindex;
    private String aName;
    private boolean sybident;
    private String extattr;
    private boolean foreign;
    private boolean isInDB;
    private boolean nullOK;
    private boolean shared;
    private boolean optional;
    private boolean kuko;
    private boolean archiv;
    private String exttable;
    private boolean isPublic;
    private boolean immutable;
    private boolean kukoonly;





    private List<dbmodel_StructShare> dbmodel_structshares;




    private dbmodel_Attribute dbmodel_attribute;




    private dbmodel_Ltype dbmodel_ltype;




    private dbmodel_StructShare dbmodel_structshare;




    private List<dbmodel_StructOverride> dbmodel_structoverrides;




    private dbmodel_Class dbmodel_class;




    private dbmodel_Attribute dbmodel_attribute;




    private dbmodel_Index dbmodel_index;


    public dbmodel_Attribute(
        String descr,        String name,        boolean kukoindex,        String aName,        boolean sybident,        String extattr,        boolean foreign,        boolean isInDB,        boolean nullOK,        boolean shared,        boolean optional,        boolean kuko,        boolean archiv,        String exttable,        boolean isPublic,        boolean immutable,        boolean kukoonly    ) {
        this.descr = descr;
        this.name = name;
        this.kukoindex = kukoindex;
        this.aName = aName;
        this.sybident = sybident;
        this.extattr = extattr;
        this.foreign = foreign;
        this.isInDB = isInDB;
        this.nullOK = nullOK;
        this.shared = shared;
        this.optional = optional;
        this.kuko = kuko;
        this.archiv = archiv;
        this.exttable = exttable;
        this.isPublic = isPublic;
        this.immutable = immutable;
        this.kukoonly = kukoonly;
        this.dbmodel_structshares = new ArrayList<>();
        this.dbmodel_structoverrides = new ArrayList<>();
    }

    public dbmodel_Attribute(
        String descr,        String name,        boolean kukoindex,        String aName,        boolean sybident,        String extattr,        boolean foreign,        boolean isInDB,        boolean nullOK,        boolean shared,        boolean optional,        boolean kuko,        boolean archiv,        String exttable,        boolean isPublic,        boolean immutable,        boolean kukoonly        ArrayList<dbmodel_StructShare> dbmodel_structshares,        ArrayList<dbmodel_StructOverride> dbmodel_structoverrides    ) {
        this.descr = descr;
        this.name = name;
        this.kukoindex = kukoindex;
        this.aName = aName;
        this.sybident = sybident;
        this.extattr = extattr;
        this.foreign = foreign;
        this.isInDB = isInDB;
        this.nullOK = nullOK;
        this.shared = shared;
        this.optional = optional;
        this.kuko = kuko;
        this.archiv = archiv;
        this.exttable = exttable;
        this.isPublic = isPublic;
        this.immutable = immutable;
        this.kukoonly = kukoonly;
        this.dbmodel_structshares = dbmodel_structshares;
        this.dbmodel_structoverrides = dbmodel_structoverrides;
    }

    public String getDescr() {
        return descr;
    }

    public void setDescr(String descr) {
        this.descr = descr;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getKukoindex() {
        return kukoindex;
    }

    public void setKukoindex(boolean kukoindex) {
        this.kukoindex = kukoindex;
    }
    public String getAname() {
        return aName;
    }

    public void setAname(String aName) {
        this.aName = aName;
    }
    public boolean getSybident() {
        return sybident;
    }

    public void setSybident(boolean sybident) {
        this.sybident = sybident;
    }
    public String getExtattr() {
        return extattr;
    }

    public void setExtattr(String extattr) {
        this.extattr = extattr;
    }
    public boolean getForeign() {
        return foreign;
    }

    public void setForeign(boolean foreign) {
        this.foreign = foreign;
    }
    public boolean getIsindb() {
        return isInDB;
    }

    public void setIsindb(boolean isInDB) {
        this.isInDB = isInDB;
    }
    public boolean getNullok() {
        return nullOK;
    }

    public void setNullok(boolean nullOK) {
        this.nullOK = nullOK;
    }
    public boolean getShared() {
        return shared;
    }

    public void setShared(boolean shared) {
        this.shared = shared;
    }
    public boolean getOptional() {
        return optional;
    }

    public void setOptional(boolean optional) {
        this.optional = optional;
    }
    public boolean getKuko() {
        return kuko;
    }

    public void setKuko(boolean kuko) {
        this.kuko = kuko;
    }
    public boolean getArchiv() {
        return archiv;
    }

    public void setArchiv(boolean archiv) {
        this.archiv = archiv;
    }
    public String getExttable() {
        return exttable;
    }

    public void setExttable(String exttable) {
        this.exttable = exttable;
    }
    public boolean getIspublic() {
        return isPublic;
    }

    public void setIspublic(boolean isPublic) {
        this.isPublic = isPublic;
    }
    public boolean getImmutable() {
        return immutable;
    }

    public void setImmutable(boolean immutable) {
        this.immutable = immutable;
    }
    public boolean getKukoonly() {
        return kukoonly;
    }

    public void setKukoonly(boolean kukoonly) {
        this.kukoonly = kukoonly;
    }

    public List<dbmodel_StructShare> getDbmodel_structshares() {
        return dbmodel_structshares;
    }

    public void addDbmodel_structshare(Dbmodel_structshare dbmodel_structshare) {
        this.dbmodel_structshares.add(dbmodel_structshare);
    }
    public dbmodel_Attribute getDbmodel_attribute() {
        return dbmodel_attribute;
    }

    public void setDbmodel_attribute(dbmodel_Attribute dbmodel_attribute) {
        this.dbmodel_attribute = dbmodel_attribute;
    }
    public dbmodel_Ltype getDbmodel_ltype() {
        return dbmodel_ltype;
    }

    public void setDbmodel_ltype(dbmodel_Ltype dbmodel_ltype) {
        this.dbmodel_ltype = dbmodel_ltype;
    }
    public dbmodel_StructShare getDbmodel_structshare() {
        return dbmodel_structshare;
    }

    public void setDbmodel_structshare(dbmodel_StructShare dbmodel_structshare) {
        this.dbmodel_structshare = dbmodel_structshare;
    }
    public List<dbmodel_StructOverride> getDbmodel_structoverrides() {
        return dbmodel_structoverrides;
    }

    public void addDbmodel_structoverride(Dbmodel_structoverride dbmodel_structoverride) {
        this.dbmodel_structoverrides.add(dbmodel_structoverride);
    }
    public dbmodel_Class getDbmodel_class() {
        return dbmodel_class;
    }

    public void setDbmodel_class(dbmodel_Class dbmodel_class) {
        this.dbmodel_class = dbmodel_class;
    }
    public dbmodel_Attribute getDbmodel_attribute() {
        return dbmodel_attribute;
    }

    public void setDbmodel_attribute(dbmodel_Attribute dbmodel_attribute) {
        this.dbmodel_attribute = dbmodel_attribute;
    }
    public dbmodel_Index getDbmodel_index() {
        return dbmodel_index;
    }

    public void setDbmodel_index(dbmodel_Index dbmodel_index) {
        this.dbmodel_index = dbmodel_index;
    }

}