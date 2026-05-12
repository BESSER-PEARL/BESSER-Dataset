





import java.util.List;
import java.util.ArrayList;

public class Requirement  {

    private String Transcript;
    private String ID_Card;
    private String Diploma;
    private String Photo;
    private String Curriculum_Vitae;





    private Registration registration;


    public Requirement(
        String Transcript,        String ID_Card,        String Diploma,        String Photo,        String Curriculum_Vitae    ) {
        this.Transcript = Transcript;
        this.ID_Card = ID_Card;
        this.Diploma = Diploma;
        this.Photo = Photo;
        this.Curriculum_Vitae = Curriculum_Vitae;
    }


    public String getTranscript() {
        return Transcript;
    }

    public void setTranscript(String Transcript) {
        this.Transcript = Transcript;
    }
    public String getId_card() {
        return ID_Card;
    }

    public void setId_card(String ID_Card) {
        this.ID_Card = ID_Card;
    }
    public String getDiploma() {
        return Diploma;
    }

    public void setDiploma(String Diploma) {
        this.Diploma = Diploma;
    }
    public String getPhoto() {
        return Photo;
    }

    public void setPhoto(String Photo) {
        this.Photo = Photo;
    }
    public String getCurriculum_vitae() {
        return Curriculum_Vitae;
    }

    public void setCurriculum_vitae(String Curriculum_Vitae) {
        this.Curriculum_Vitae = Curriculum_Vitae;
    }

    public Registration getRegistration() {
        return registration;
    }

    public void setRegistration(Registration registration) {
        this.registration = registration;
    }

}