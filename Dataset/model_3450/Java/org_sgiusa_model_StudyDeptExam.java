





import java.util.List;
import java.util.ArrayList;

public class org_sgiusa_model_StudyDeptExam  {

    private String examDate;
    private String examLocation;
    private String examLanguage;
    private String examLevel;
    private String id;
    private String lastUpdate;
    private String current;



    public org_sgiusa_model_StudyDeptExam(
        String examDate,        String examLocation,        String examLanguage,        String examLevel,        String id,        String lastUpdate,        String current    ) {
        this.examDate = examDate;
        this.examLocation = examLocation;
        this.examLanguage = examLanguage;
        this.examLevel = examLevel;
        this.id = id;
        this.lastUpdate = lastUpdate;
        this.current = current;
    }


    public String getExamdate() {
        return examDate;
    }

    public void setExamdate(String examDate) {
        this.examDate = examDate;
    }
    public String getExamlocation() {
        return examLocation;
    }

    public void setExamlocation(String examLocation) {
        this.examLocation = examLocation;
    }
    public String getExamlanguage() {
        return examLanguage;
    }

    public void setExamlanguage(String examLanguage) {
        this.examLanguage = examLanguage;
    }
    public String getExamlevel() {
        return examLevel;
    }

    public void setExamlevel(String examLevel) {
        this.examLevel = examLevel;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getLastupdate() {
        return lastUpdate;
    }

    public void setLastupdate(String lastUpdate) {
        this.lastUpdate = lastUpdate;
    }
    public String getCurrent() {
        return current;
    }

    public void setCurrent(String current) {
        this.current = current;
    }


}