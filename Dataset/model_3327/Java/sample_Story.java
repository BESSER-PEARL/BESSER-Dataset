





import java.util.List;
import java.util.ArrayList;

public class sample_Story  {

    private String Title;
    private String Feature;
    private String Role;
    private String Benefit;



    public sample_Story(
        String Title,        String Feature,        String Role,        String Benefit    ) {
        this.Title = Title;
        this.Feature = Feature;
        this.Role = Role;
        this.Benefit = Benefit;
    }


    public String getTitle() {
        return Title;
    }

    public void setTitle(String Title) {
        this.Title = Title;
    }
    public String getFeature() {
        return Feature;
    }

    public void setFeature(String Feature) {
        this.Feature = Feature;
    }
    public String getRole() {
        return Role;
    }

    public void setRole(String Role) {
        this.Role = Role;
    }
    public String getBenefit() {
        return Benefit;
    }

    public void setBenefit(String Benefit) {
        this.Benefit = Benefit;
    }


}