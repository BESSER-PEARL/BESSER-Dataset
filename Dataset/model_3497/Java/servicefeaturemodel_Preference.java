




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class servicefeaturemodel_Preference  {

    private float value;
    private String description;
    private LocalDate creationDate;
    private String stakeholderGroup;





    private servicefeaturemodel_Configuration servicefeaturemodel_configuration;


    public servicefeaturemodel_Preference(
        float value,        String description,        LocalDate creationDate,        String stakeholderGroup    ) {
        this.value = value;
        this.description = description;
        this.creationDate = creationDate;
        this.stakeholderGroup = stakeholderGroup;
    }


    public float getValue() {
        return value;
    }

    public void setValue(float value) {
        this.value = value;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public LocalDate getCreationdate() {
        return creationDate;
    }

    public void setCreationdate(LocalDate creationDate) {
        this.creationDate = creationDate;
    }
    public String getStakeholdergroup() {
        return stakeholderGroup;
    }

    public void setStakeholdergroup(String stakeholderGroup) {
        this.stakeholderGroup = stakeholderGroup;
    }

    public servicefeaturemodel_Configuration getServicefeaturemodel_configuration() {
        return servicefeaturemodel_configuration;
    }

    public void setServicefeaturemodel_configuration(servicefeaturemodel_Configuration servicefeaturemodel_configuration) {
        this.servicefeaturemodel_configuration = servicefeaturemodel_configuration;
    }

}