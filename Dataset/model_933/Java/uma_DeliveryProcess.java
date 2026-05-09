





import java.util.List;
import java.util.ArrayList;

public class uma_DeliveryProcess extends Process {

    private String communicationsMaterial;
    private String educationMaterial;
    private String group4;



    public uma_DeliveryProcess(
        String communicationsMaterial,        String educationMaterial,        String group4    ) {
        super(
        );
        this.communicationsMaterial = communicationsMaterial;
        this.educationMaterial = educationMaterial;
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
    public String getGroup4() {
        return group4;
    }

    public void setGroup4(String group4) {
        this.group4 = group4;
    }


}