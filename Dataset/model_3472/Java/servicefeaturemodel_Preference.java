




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class servicefeaturemodel_Preference  {

    private String stakeholderGroup;
    private String description;
    private float value;
    private LocalDate creationDate;





    private servicefeaturemodel_Configuration servicefeaturemodel_configuration;


    public servicefeaturemodel_Preference(
        String stakeholderGroup,        String description,        float value,        LocalDate creationDate    ) {
        this.stakeholderGroup = stakeholderGroup;
        this.description = description;
        this.value = value;
        this.creationDate = creationDate;
    }


    public String getStakeholdergroup() {
        return stakeholderGroup;
    }

    public void setStakeholdergroup(String stakeholderGroup) {
        this.stakeholderGroup = stakeholderGroup;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public float getValue() {
        return value;
    }

    public void setValue(float value) {
        this.value = value;
    }
    public LocalDate getCreationdate() {
        return creationDate;
    }

    public void setCreationdate(LocalDate creationDate) {
        this.creationDate = creationDate;
    }

    public servicefeaturemodel_Configuration getServicefeaturemodel_configuration() {
        return servicefeaturemodel_configuration;
    }

    public void setServicefeaturemodel_configuration(servicefeaturemodel_Configuration servicefeaturemodel_configuration) {
        this.servicefeaturemodel_configuration = servicefeaturemodel_configuration;
    }

}