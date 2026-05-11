





import java.util.List;
import java.util.ArrayList;

public class VorkursModel_Qualification  {

    private boolean hasPCExperience;
    private String Language;
    private boolean hasProgrammingExperience;
    private String programminLanguage;



    public VorkursModel_Qualification(
        boolean hasPCExperience,        String Language,        boolean hasProgrammingExperience,        String programminLanguage    ) {
        this.hasPCExperience = hasPCExperience;
        this.Language = Language;
        this.hasProgrammingExperience = hasProgrammingExperience;
        this.programminLanguage = programminLanguage;
    }


    public boolean getHaspcexperience() {
        return hasPCExperience;
    }

    public void setHaspcexperience(boolean hasPCExperience) {
        this.hasPCExperience = hasPCExperience;
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
    public String getProgramminlanguage() {
        return programminLanguage;
    }

    public void setProgramminlanguage(String programminLanguage) {
        this.programminLanguage = programminLanguage;
    }


}