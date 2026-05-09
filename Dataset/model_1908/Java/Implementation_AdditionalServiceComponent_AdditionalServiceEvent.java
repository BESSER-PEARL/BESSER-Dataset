




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Implementation_AdditionalServiceComponent_AdditionalServiceEvent  {

    private String location;
    private String maxAttendant;
    private LocalDate dateTime;
    private String currentAttendants;





    private Implementation_AdditionalServiceComponent_AdditionalService implementation_additionalservicecomponent_additionalservice;




    private Implementation_AdditionalServiceComponent_AdditionalService implementation_additionalservicecomponent_additionalservice;


    public Implementation_AdditionalServiceComponent_AdditionalServiceEvent(
        String location,        String maxAttendant,        LocalDate dateTime,        String currentAttendants    ) {
        this.location = location;
        this.maxAttendant = maxAttendant;
        this.dateTime = dateTime;
        this.currentAttendants = currentAttendants;
    }


    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getMaxattendant() {
        return maxAttendant;
    }

    public void setMaxattendant(String maxAttendant) {
        this.maxAttendant = maxAttendant;
    }
    public LocalDate getDatetime() {
        return dateTime;
    }

    public void setDatetime(LocalDate dateTime) {
        this.dateTime = dateTime;
    }
    public String getCurrentattendants() {
        return currentAttendants;
    }

    public void setCurrentattendants(String currentAttendants) {
        this.currentAttendants = currentAttendants;
    }

    public Implementation_AdditionalServiceComponent_AdditionalService getImplementation_additionalservicecomponent_additionalservice() {
        return implementation_additionalservicecomponent_additionalservice;
    }

    public void setImplementation_additionalservicecomponent_additionalservice(Implementation_AdditionalServiceComponent_AdditionalService implementation_additionalservicecomponent_additionalservice) {
        this.implementation_additionalservicecomponent_additionalservice = implementation_additionalservicecomponent_additionalservice;
    }
    public Implementation_AdditionalServiceComponent_AdditionalService getImplementation_additionalservicecomponent_additionalservice() {
        return implementation_additionalservicecomponent_additionalservice;
    }

    public void setImplementation_additionalservicecomponent_additionalservice(Implementation_AdditionalServiceComponent_AdditionalService implementation_additionalservicecomponent_additionalservice) {
        this.implementation_additionalservicecomponent_additionalservice = implementation_additionalservicecomponent_additionalservice;
    }

}