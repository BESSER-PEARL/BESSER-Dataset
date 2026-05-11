




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class contentfwk_Standard  {

    private String standardClass;
    private LocalDate retireDate;
    private LocalDate standardCreationDate;
    private LocalDate lastStandardCreationDate;
    private LocalDate nextStandardCreationDate;



    public contentfwk_Standard(
        String standardClass,        LocalDate retireDate,        LocalDate standardCreationDate,        LocalDate lastStandardCreationDate,        LocalDate nextStandardCreationDate    ) {
        this.standardClass = standardClass;
        this.retireDate = retireDate;
        this.standardCreationDate = standardCreationDate;
        this.lastStandardCreationDate = lastStandardCreationDate;
        this.nextStandardCreationDate = nextStandardCreationDate;
    }


    public String getStandardclass() {
        return standardClass;
    }

    public void setStandardclass(String standardClass) {
        this.standardClass = standardClass;
    }
    public LocalDate getRetiredate() {
        return retireDate;
    }

    public void setRetiredate(LocalDate retireDate) {
        this.retireDate = retireDate;
    }
    public LocalDate getStandardcreationdate() {
        return standardCreationDate;
    }

    public void setStandardcreationdate(LocalDate standardCreationDate) {
        this.standardCreationDate = standardCreationDate;
    }
    public LocalDate getLaststandardcreationdate() {
        return lastStandardCreationDate;
    }

    public void setLaststandardcreationdate(LocalDate lastStandardCreationDate) {
        this.lastStandardCreationDate = lastStandardCreationDate;
    }
    public LocalDate getNextstandardcreationdate() {
        return nextStandardCreationDate;
    }

    public void setNextstandardcreationdate(LocalDate nextStandardCreationDate) {
        this.nextStandardCreationDate = nextStandardCreationDate;
    }


}