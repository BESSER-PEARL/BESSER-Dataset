




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class model_STEMTime  {

    private LocalDate time;



    public model_STEMTime(
        LocalDate time    ) {
        this.time = time;
    }


    public LocalDate getTime() {
        return time;
    }

    public void setTime(LocalDate time) {
        this.time = time;
    }


}