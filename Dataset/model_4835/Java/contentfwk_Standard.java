




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class contentfwk_Standard  {

    private LocalDate lastStandardReviewDate;
    private LocalDate standardCreationDate;
    private String standardClass;
    private LocalDate retireDate;
    private LocalDate nextStandardReviewDate;



    public contentfwk_Standard(
        LocalDate lastStandardReviewDate,        LocalDate standardCreationDate,        String standardClass,        LocalDate retireDate,        LocalDate nextStandardReviewDate    ) {
        this.lastStandardReviewDate = lastStandardReviewDate;
        this.standardCreationDate = standardCreationDate;
        this.standardClass = standardClass;
        this.retireDate = retireDate;
        this.nextStandardReviewDate = nextStandardReviewDate;
    }


    public LocalDate getLaststandardreviewdate() {
        return lastStandardReviewDate;
    }

    public void setLaststandardreviewdate(LocalDate lastStandardReviewDate) {
        this.lastStandardReviewDate = lastStandardReviewDate;
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
    public LocalDate getRetiredate() {
        return retireDate;
    }

    public void setRetiredate(LocalDate retireDate) {
        this.retireDate = retireDate;
    }
    public LocalDate getNextstandardreviewdate() {
        return nextStandardReviewDate;
    }

    public void setNextstandardreviewdate(LocalDate nextStandardReviewDate) {
        this.nextStandardReviewDate = nextStandardReviewDate;
    }


}