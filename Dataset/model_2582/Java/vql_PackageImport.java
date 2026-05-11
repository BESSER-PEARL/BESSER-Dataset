





import java.util.List;
import java.util.ArrayList;

public class vql_PackageImport  {

    private String alias;





    private vql_VQLImportSection vql_vqlimportsection;




    private vql_ClassType vql_classtype;


    public vql_PackageImport(
        String alias    ) {
        this.alias = alias;
    }


    public String getAlias() {
        return alias;
    }

    public void setAlias(String alias) {
        this.alias = alias;
    }

    public vql_VQLImportSection getVql_vqlimportsection() {
        return vql_vqlimportsection;
    }

    public void setVql_vqlimportsection(vql_VQLImportSection vql_vqlimportsection) {
        this.vql_vqlimportsection = vql_vqlimportsection;
    }
    public vql_ClassType getVql_classtype() {
        return vql_classtype;
    }

    public void setVql_classtype(vql_ClassType vql_classtype) {
        this.vql_classtype = vql_classtype;
    }

}