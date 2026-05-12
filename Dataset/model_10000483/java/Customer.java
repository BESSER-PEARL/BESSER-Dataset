




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private LocalDate recruitmentDate;



    public Customer(
        LocalDate recruitmentDate    ) {
        this.recruitmentDate = recruitmentDate;
    }


    public LocalDate getRecruitmentdate() {
        return recruitmentDate;
    }

    public void setRecruitmentdate(LocalDate recruitmentDate) {
        this.recruitmentDate = recruitmentDate;
    }


}