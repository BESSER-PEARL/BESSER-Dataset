




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class esmodel_versioning_DateVersionSpec extends VersionSpec {

    private LocalDate date;



    public esmodel_versioning_DateVersionSpec(
        LocalDate date    ) {
        super(
        );
        this.date = date;
    }


    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }


}