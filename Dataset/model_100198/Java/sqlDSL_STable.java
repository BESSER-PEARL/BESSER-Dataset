





import java.util.List;
import java.util.ArrayList;

public class sqlDSL_STable extends SArtifact {

    private boolean cached;
    private String prefix;
    private String entityname;





    private sqlDSL_SJoinColumn sqldsl_sjoincolumn;




    private sqlDSL_SSettings sqldsl_ssettings;




    private List<sqlDSL_STableMember> sqldsl_stablemembers;


    public sqlDSL_STable(
        boolean cached,        String prefix,        String entityname    ) {
        super(
        );
        this.cached = cached;
        this.prefix = prefix;
        this.entityname = entityname;
        this.sqldsl_stablemembers = new ArrayList<>();
    }

    public sqlDSL_STable(
        boolean cached,        String prefix,        String entityname        ArrayList<sqlDSL_STableMember> sqldsl_stablemembers    ) {
        this.cached = cached;
        this.prefix = prefix;
        this.entityname = entityname;
        this.sqldsl_stablemembers = sqldsl_stablemembers;
    }

    public boolean getCached() {
        return cached;
    }

    public void setCached(boolean cached) {
        this.cached = cached;
    }
    public String getPrefix() {
        return prefix;
    }

    public void setPrefix(String prefix) {
        this.prefix = prefix;
    }
    public String getEntityname() {
        return entityname;
    }

    public void setEntityname(String entityname) {
        this.entityname = entityname;
    }

    public sqlDSL_SJoinColumn getSqldsl_sjoincolumn() {
        return sqldsl_sjoincolumn;
    }

    public void setSqldsl_sjoincolumn(sqlDSL_SJoinColumn sqldsl_sjoincolumn) {
        this.sqldsl_sjoincolumn = sqldsl_sjoincolumn;
    }
    public sqlDSL_SSettings getSqldsl_ssettings() {
        return sqldsl_ssettings;
    }

    public void setSqldsl_ssettings(sqlDSL_SSettings sqldsl_ssettings) {
        this.sqldsl_ssettings = sqldsl_ssettings;
    }
    public List<sqlDSL_STableMember> getSqldsl_stablemembers() {
        return sqldsl_stablemembers;
    }

    public void addSqldsl_stablemember(Sqldsl_stablemember sqldsl_stablemember) {
        this.sqldsl_stablemembers.add(sqldsl_stablemember);
    }

}