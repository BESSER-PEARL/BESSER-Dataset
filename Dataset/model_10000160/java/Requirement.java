





import java.util.List;
import java.util.ArrayList;

public class Requirement  {

    private String Photo;
    private String Curriculum_Vitae;
    private String ID_Card;
    private String Transcript;
    private String Diploma;





    private Registration registration;


    public Requirement(
        String Photo,        String Curriculum_Vitae,        String ID_Card,        String Transcript,        String Diploma    ) {
        this.Photo = Photo;
        this.Curriculum_Vitae = Curriculum_Vitae;
        this.ID_Card = ID_Card;
        this.Transcript = Transcript;
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
    public String getId_card() {
        return ID_Card;
    }

    public void setId_card(String ID_Card) {
        this.ID_Card = ID_Card;
    }
    public String getTranscript() {
        return Transcript;
    }

    public void setTranscript(String Transcript) {
        this.Transcript = Transcript;
    }
    public String getDiploma() {
        return Diploma;
    }

    public void setDiploma(String Diploma) {
        this.Diploma = Diploma;
    }

    public Registration getRegistration() {
        return registration;
    }

    public void setRegistration(Registration registration) {
        this.registration = registration;
    }

}