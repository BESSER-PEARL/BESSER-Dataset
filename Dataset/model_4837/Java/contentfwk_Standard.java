




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class contentfwk_Standard  {

    private String retireDate;
    private LocalDate lastStandardCreationDate;
    private LocalDate standardCreationDate;
    private String standardClass;
    private LocalDate nextStandardCreationDate;



    public contentfwk_Standard(
        String retireDate,        LocalDate lastStandardCreationDate,        LocalDate standardCreationDate,        String standardClass,        LocalDate nextStandardCreationDate    ) {
        this.retireDate = retireDate;
        this.lastStandardCreationDate = lastStandardCreationDate;
        this.standardCreationDate = standardCreationDate;
        this.standardClass = standardClass;
        this.nextStandardCreationDate = nextStandardCreationDate;
    }


    public String getRetiredate() {
        return retireDate;
    }

    public void setRetiredate(String retireDate) {
        this.retireDate = retireDate;
    }
    public LocalDate getLaststandardcreationdate() {
        return lastStandardCreationDate;
    }

    public void setLaststandardcreationdate(LocalDate lastStandardCreationDate) {
        this.lastStandardCreationDate = lastStandardCreationDate;
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
    public LocalDate getNextstandardcreationdate() {
        return nextStandardCreationDate;
    }

    public void setNextstandardcreationdate(LocalDate nextStandardCreationDate) {
        this.nextStandardCreationDate = nextStandardCreationDate;
    }


}