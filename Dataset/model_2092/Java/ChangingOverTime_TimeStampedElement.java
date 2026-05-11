




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class ChangingOverTime_TimeStampedElement  {

    private LocalDate effectiveDate;
    private LocalDate expirationDate;



    public ChangingOverTime_TimeStampedElement(
        LocalDate effectiveDate,        LocalDate expirationDate    ) {
        this.effectiveDate = effectiveDate;
        this.expirationDate = expirationDate;
    }


    public LocalDate getEffectivedate() {
        return effectiveDate;
    }

    public void setEffectivedate(LocalDate effectiveDate) {
        this.effectiveDate = effectiveDate;
    }
    public LocalDate getExpirationdate() {
        return expirationDate;
    }

    public void setExpirationdate(LocalDate expirationDate) {
        this.expirationDate = expirationDate;
    }


}