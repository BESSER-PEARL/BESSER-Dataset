




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class collection_SmartInformationObjectCollection extends ItemsCollection {

    private String includeContents;
    private LocalDate minimumAge;
    private String includePersons;
    private String includeOrganisations;



    public collection_SmartInformationObjectCollection(
        String includeContents,        LocalDate minimumAge,        String includePersons,        String includeOrganisations    ) {
        super(
        );
        this.includeContents = includeContents;
        this.minimumAge = minimumAge;
        this.includePersons = includePersons;
        this.includeOrganisations = includeOrganisations;
    }


    public String getIncludecontents() {
        return includeContents;
    }

    public void setIncludecontents(String includeContents) {
        this.includeContents = includeContents;
    }
    public LocalDate getMinimumage() {
        return minimumAge;
    }

    public void setMinimumage(LocalDate minimumAge) {
        this.minimumAge = minimumAge;
    }
    public String getIncludepersons() {
        return includePersons;
    }

    public void setIncludepersons(String includePersons) {
        this.includePersons = includePersons;
    }
    public String getIncludeorganisations() {
        return includeOrganisations;
    }

    public void setIncludeorganisations(String includeOrganisations) {
        this.includeOrganisations = includeOrganisations;
    }


}