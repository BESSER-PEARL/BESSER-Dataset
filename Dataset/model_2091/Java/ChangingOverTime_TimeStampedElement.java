




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class ChangingOverTime_TimeStampedElement  {

    private LocalDate expirationDate;
    private LocalDate effectiveDate;



    public ChangingOverTime_TimeStampedElement(
        LocalDate expirationDate,        LocalDate effectiveDate    ) {
        this.expirationDate = expirationDate;
        this.effectiveDate = effectiveDate;
    }


    public LocalDate getExpirationdate() {
        return expirationDate;
    }

    public void setExpirationdate(LocalDate expirationDate) {
        this.expirationDate = expirationDate;
    }
    public LocalDate getEffectivedate() {
        return effectiveDate;
    }

    public void setEffectivedate(LocalDate effectiveDate) {
        this.effectiveDate = effectiveDate;
    }


}