





import java.util.List;
import java.util.ArrayList;

public class dbmodel_Class extends ClassOrDuplicate {

    private String aName;
    private String descr;
    private String whereclause;
    private String archivIndex;
    private boolean pubspec;
    private boolean noDBio;
    private int vmaj;
    private boolean publish;
    private String pubname;
    private int vmin;





    private dbmodel_Subject dbmodel_subject;


    public dbmodel_Class(
        String aName,        String descr,        String whereclause,        String archivIndex,        boolean pubspec,        boolean noDBio,        int vmaj,        boolean publish,        String pubname,        int vmin    ) {
        super(
        );
        this.aName = aName;
        this.descr = descr;
        this.whereclause = whereclause;
        this.archivIndex = archivIndex;
        this.pubspec = pubspec;
        this.noDBio = noDBio;
        this.vmaj = vmaj;
        this.publish = publish;
        this.pubname = pubname;
        this.vmin = vmin;
    }


    public String getAname() {
        return aName;
    }

    public void setAname(String aName) {
        this.aName = aName;
    }
    public String getDescr() {
        return descr;
    }

    public void setDescr(String descr) {
        this.descr = descr;
    }
    public String getWhereclause() {
        return whereclause;
    }

    public void setWhereclause(String whereclause) {
        this.whereclause = whereclause;
    }
    public String getArchivindex() {
        return archivIndex;
    }

    public void setArchivindex(String archivIndex) {
        this.archivIndex = archivIndex;
    }
    public boolean getPubspec() {
        return pubspec;
    }

    public void setPubspec(boolean pubspec) {
        this.pubspec = pubspec;
    }
    public boolean getNodbio() {
        return noDBio;
    }

    public void setNodbio(boolean noDBio) {
        this.noDBio = noDBio;
    }
    public int getVmaj() {
        return vmaj;
    }

    public void setVmaj(int vmaj) {
        this.vmaj = vmaj;
    }
    public boolean getPublish() {
        return publish;
    }

    public void setPublish(boolean publish) {
        this.publish = publish;
    }
    public String getPubname() {
        return pubname;
    }

    public void setPubname(String pubname) {
        this.pubname = pubname;
    }
    public int getVmin() {
        return vmin;
    }

    public void setVmin(int vmin) {
        this.vmin = vmin;
    }

    public dbmodel_Subject getDbmodel_subject() {
        return dbmodel_subject;
    }

    public void setDbmodel_subject(dbmodel_Subject dbmodel_subject) {
        this.dbmodel_subject = dbmodel_subject;
    }

}