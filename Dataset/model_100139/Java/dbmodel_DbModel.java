





import java.util.List;
import java.util.ArrayList;

public class dbmodel_DbModel  {

    private boolean doAll;
    private String name;
    private String kudaType;
    private String kobeType;
    private String version;
    private String mtype;





    private List<dbmodel_Class> dbmodel_classs;




    private List<dbmodel_Import> dbmodel_imports;




    private List<dbmodel_Subject> dbmodel_subjects;




    private List<dbmodel_Duplicate> dbmodel_duplicates;


    public dbmodel_DbModel(
        boolean doAll,        String name,        String kudaType,        String kobeType,        String version,        String mtype    ) {
        this.doAll = doAll;
        this.name = name;
        this.kudaType = kudaType;
        this.kobeType = kobeType;
        this.version = version;
        this.mtype = mtype;
        this.dbmodel_classs = new ArrayList<>();
        this.dbmodel_imports = new ArrayList<>();
        this.dbmodel_subjects = new ArrayList<>();
        this.dbmodel_duplicates = new ArrayList<>();
    }

    public dbmodel_DbModel(
        boolean doAll,        String name,        String kudaType,        String kobeType,        String version,        String mtype        ArrayList<dbmodel_Class> dbmodel_classs,        ArrayList<dbmodel_Import> dbmodel_imports,        ArrayList<dbmodel_Subject> dbmodel_subjects,        ArrayList<dbmodel_Duplicate> dbmodel_duplicates    ) {
        this.doAll = doAll;
        this.name = name;
        this.kudaType = kudaType;
        this.kobeType = kobeType;
        this.version = version;
        this.mtype = mtype;
        this.dbmodel_classs = dbmodel_classs;
        this.dbmodel_imports = dbmodel_imports;
        this.dbmodel_subjects = dbmodel_subjects;
        this.dbmodel_duplicates = dbmodel_duplicates;
    }

    public boolean getDoall() {
        return doAll;
    }

    public void setDoall(boolean doAll) {
        this.doAll = doAll;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getKudatype() {
        return kudaType;
    }

    public void setKudatype(String kudaType) {
        this.kudaType = kudaType;
    }
    public String getKobetype() {
        return kobeType;
    }

    public void setKobetype(String kobeType) {
        this.kobeType = kobeType;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getMtype() {
        return mtype;
    }

    public void setMtype(String mtype) {
        this.mtype = mtype;
    }

    public List<dbmodel_Class> getDbmodel_classs() {
        return dbmodel_classs;
    }

    public void addDbmodel_class(Dbmodel_class dbmodel_class) {
        this.dbmodel_classs.add(dbmodel_class);
    }
    public List<dbmodel_Import> getDbmodel_imports() {
        return dbmodel_imports;
    }

    public void addDbmodel_import(Dbmodel_import dbmodel_import) {
        this.dbmodel_imports.add(dbmodel_import);
    }
    public List<dbmodel_Subject> getDbmodel_subjects() {
        return dbmodel_subjects;
    }

    public void addDbmodel_subject(Dbmodel_subject dbmodel_subject) {
        this.dbmodel_subjects.add(dbmodel_subject);
    }
    public List<dbmodel_Duplicate> getDbmodel_duplicates() {
        return dbmodel_duplicates;
    }

    public void addDbmodel_duplicate(Dbmodel_duplicate dbmodel_duplicate) {
        this.dbmodel_duplicates.add(dbmodel_duplicate);
    }

}