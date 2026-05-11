




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class feature_HyFeature extends HyTemporalElement, HyNamedElement {

    private LocalDate deprecatedSince;



    public feature_HyFeature(
        LocalDate deprecatedSince    ) {
        super(
        );
        this.deprecatedSince = deprecatedSince;
    }


    public LocalDate getDeprecatedsince() {
        return deprecatedSince;
    }

    public void setDeprecatedsince(LocalDate deprecatedSince) {
        this.deprecatedSince = deprecatedSince;
    }


}