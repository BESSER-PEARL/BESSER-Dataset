




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class requirements_RequirementsDefinition extends Organization {

    private LocalDate date;
    private String version;



    public requirements_RequirementsDefinition(
        LocalDate date,        String version    ) {
        super(
        );
        this.date = date;
        this.version = version;
    }


    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }


}