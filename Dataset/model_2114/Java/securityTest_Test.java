




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class securityTest_Test  {

    private String name;
    private LocalDate date;
    private String severity;
    private String id;



    public securityTest_Test(
        String name,        LocalDate date,        String severity,        String id    ) {
        this.name = name;
        this.date = date;
        this.severity = severity;
        this.id = id;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }
    public String getSeverity() {
        return severity;
    }

    public void setSeverity(String severity) {
        this.severity = severity;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}