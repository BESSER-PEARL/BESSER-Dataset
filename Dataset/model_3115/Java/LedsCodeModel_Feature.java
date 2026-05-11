





import java.util.List;
import java.util.ArrayList;

public class LedsCodeModel_Feature  {

    private String language;
    private String engine;
    private String orm;
    private String applicationType;
    private String dataBaseName;





    private LedsCodeModel_Specification ledscodemodel_specification;


    public LedsCodeModel_Feature(
        String language,        String engine,        String orm,        String applicationType,        String dataBaseName    ) {
        this.language = language;
        this.engine = engine;
        this.orm = orm;
        this.applicationType = applicationType;
        this.dataBaseName = dataBaseName;
    }


    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }
    public String getEngine() {
        return engine;
    }

    public void setEngine(String engine) {
        this.engine = engine;
    }
    public String getOrm() {
        return orm;
    }

    public void setOrm(String orm) {
        this.orm = orm;
    }
    public String getApplicationtype() {
        return applicationType;
    }

    public void setApplicationtype(String applicationType) {
        this.applicationType = applicationType;
    }
    public String getDatabasename() {
        return dataBaseName;
    }

    public void setDatabasename(String dataBaseName) {
        this.dataBaseName = dataBaseName;
    }

    public LedsCodeModel_Specification getLedscodemodel_specification() {
        return ledscodemodel_specification;
    }

    public void setLedscodemodel_specification(LedsCodeModel_Specification ledscodemodel_specification) {
        this.ledscodemodel_specification = ledscodemodel_specification;
    }

}