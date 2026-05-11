




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class LedsCodeModel_Specification  {

    private String name;
    private LocalDate createdDate;



    public LedsCodeModel_Specification(
        String name,        LocalDate createdDate    ) {
        this.name = name;
        this.createdDate = createdDate;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public LocalDate getCreateddate() {
        return createdDate;
    }

    public void setCreateddate(LocalDate createdDate) {
        this.createdDate = createdDate;
    }


}