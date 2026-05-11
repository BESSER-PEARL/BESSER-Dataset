




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class contentfwk_Standard  {

    private LocalDate standardCreationDate;
    private LocalDate nextStandardCreationDate;
    private LocalDate retireDate;
    private LocalDate lastStandardCreationDate;
    private String standardClass;



    public contentfwk_Standard(
        LocalDate standardCreationDate,        LocalDate nextStandardCreationDate,        LocalDate retireDate,        LocalDate lastStandardCreationDate,        String standardClass    ) {
        this.standardCreationDate = standardCreationDate;
        this.nextStandardCreationDate = nextStandardCreationDate;
        this.retireDate = retireDate;
        this.lastStandardCreationDate = lastStandardCreationDate;
        this.standardClass = standardClass;
    }


    public LocalDate getStandardcreationdate() {
        return standardCreationDate;
    }

    public void setStandardcreationdate(LocalDate standardCreationDate) {
        this.standardCreationDate = standardCreationDate;
    }
    public LocalDate getNextstandardcreationdate() {
        return nextStandardCreationDate;
    }

    public void setNextstandardcreationdate(LocalDate nextStandardCreationDate) {
        this.nextStandardCreationDate = nextStandardCreationDate;
    }
    public LocalDate getRetiredate() {
        return retireDate;
    }

    public void setRetiredate(LocalDate retireDate) {
        this.retireDate = retireDate;
    }
    public LocalDate getLaststandardcreationdate() {
        return lastStandardCreationDate;
    }

    public void setLaststandardcreationdate(LocalDate lastStandardCreationDate) {
        this.lastStandardCreationDate = lastStandardCreationDate;
    }
    public String getStandardclass() {
        return standardClass;
    }

    public void setStandardclass(String standardClass) {
        this.standardClass = standardClass;
    }


}