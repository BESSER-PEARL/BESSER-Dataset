




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class contentfwk_Standard  {

    private LocalDate nextStandardCreationDate;
    private LocalDate standardCreationDate;
    private String standardClass;
    private LocalDate lastStandardCreationDate;
    private LocalDate retireDate;



    public contentfwk_Standard(
        LocalDate nextStandardCreationDate,        LocalDate standardCreationDate,        String standardClass,        LocalDate lastStandardCreationDate,        LocalDate retireDate    ) {
        this.nextStandardCreationDate = nextStandardCreationDate;
        this.standardCreationDate = standardCreationDate;
        this.standardClass = standardClass;
        this.lastStandardCreationDate = lastStandardCreationDate;
        this.retireDate = retireDate;
    }


    public LocalDate getNextstandardcreationdate() {
        return nextStandardCreationDate;
    }

    public void setNextstandardcreationdate(LocalDate nextStandardCreationDate) {
        this.nextStandardCreationDate = nextStandardCreationDate;
    }
    public LocalDate getStandardcreationdate() {
        return standardCreationDate;
    }

    public void setStandardcreationdate(LocalDate standardCreationDate) {
        this.standardCreationDate = standardCreationDate;
    }
    public String getStandardclass() {
        return standardClass;
    }

    public void setStandardclass(String standardClass) {
        this.standardClass = standardClass;
    }
    public LocalDate getLaststandardcreationdate() {
        return lastStandardCreationDate;
    }

    public void setLaststandardcreationdate(LocalDate lastStandardCreationDate) {
        this.lastStandardCreationDate = lastStandardCreationDate;
    }
    public LocalDate getRetiredate() {
        return retireDate;
    }

    public void setRetiredate(LocalDate retireDate) {
        this.retireDate = retireDate;
    }


}