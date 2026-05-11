





import java.util.List;
import java.util.ArrayList;

public class VorkursModel_Qualification  {

    private String programminLanguage;
    private String Language;
    private boolean hasProgrammingExperience;
    private boolean hasPCExperience;





    private VorkursModel_Person vorkursmodel_person;


    public VorkursModel_Qualification(
        String programminLanguage,        String Language,        boolean hasProgrammingExperience,        boolean hasPCExperience    ) {
        this.programminLanguage = programminLanguage;
        this.Language = Language;
        this.hasProgrammingExperience = hasProgrammingExperience;
        this.hasPCExperience = hasPCExperience;
    }


    public String getProgramminlanguage() {
        return programminLanguage;
    }

    public void setProgramminlanguage(String programminLanguage) {
        this.programminLanguage = programminLanguage;
    }
    public String getLanguage() {
        return Language;
    }

    public void setLanguage(String Language) {
        this.Language = Language;
    }
    public boolean getHasprogrammingexperience() {
        return hasProgrammingExperience;
    }

    public void setHasprogrammingexperience(boolean hasProgrammingExperience) {
        this.hasProgrammingExperience = hasProgrammingExperience;
    }
    public boolean getHaspcexperience() {
        return hasPCExperience;
    }

    public void setHaspcexperience(boolean hasPCExperience) {
        this.hasPCExperience = hasPCExperience;
    }

    public VorkursModel_Person getVorkursmodel_person() {
        return vorkursmodel_person;
    }

    public void setVorkursmodel_person(VorkursModel_Person vorkursmodel_person) {
        this.vorkursmodel_person = vorkursmodel_person;
    }

}