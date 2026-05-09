





import java.util.List;
import java.util.ArrayList;

public class uma_DeliveryProcess extends Process {

    private String group4;
    private String communicationsMaterial;
    private String educationMaterial;



    public uma_DeliveryProcess(
        String group4,        String communicationsMaterial,        String educationMaterial    ) {
        super(
        );
        this.group4 = group4;
        this.communicationsMaterial = communicationsMaterial;
        this.educationMaterial = educationMaterial;
    }


    public String getGroup4() {
        return group4;
    }

    public void setGroup4(String group4) {
        this.group4 = group4;
    }
    public String getCommunicationsmaterial() {
        return communicationsMaterial;
    }

    public void setCommunicationsmaterial(String communicationsMaterial) {
        this.communicationsMaterial = communicationsMaterial;
    }
    public String getEducationmaterial() {
        return educationMaterial;
    }

    public void setEducationmaterial(String educationMaterial) {
        this.educationMaterial = educationMaterial;
    }


}