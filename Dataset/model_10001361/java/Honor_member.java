





import java.util.List;
import java.util.ArrayList;

public class Honor_member  {

    private String Member_start_date;
    private int Amount_of_partnership;



    public Honor_member(
        String Member_start_date,        int Amount_of_partnership    ) {
        this.Member_start_date = Member_start_date;
        this.Amount_of_partnership = Amount_of_partnership;
    }


    public String getMember_start_date() {
        return Member_start_date;
    }

    public void setMember_start_date(String Member_start_date) {
        this.Member_start_date = Member_start_date;
    }
    public int getAmount_of_partnership() {
        return Amount_of_partnership;
    }

    public void setAmount_of_partnership(int Amount_of_partnership) {
        this.Amount_of_partnership = Amount_of_partnership;
    }


}