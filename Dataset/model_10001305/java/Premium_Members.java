





import java.util.List;
import java.util.ArrayList;

public class Premium_Members  {

    private String MembershipEndDate;
    private String MembershipStartDate;
    private String PromoCode;



    public Premium_Members(
        String MembershipEndDate,        String MembershipStartDate,        String PromoCode    ) {
        this.MembershipEndDate = MembershipEndDate;
        this.MembershipStartDate = MembershipStartDate;
        this.PromoCode = PromoCode;
    }


    public String getMembershipenddate() {
        return MembershipEndDate;
    }

    public void setMembershipenddate(String MembershipEndDate) {
        this.MembershipEndDate = MembershipEndDate;
    }
    public String getMembershipstartdate() {
        return MembershipStartDate;
    }

    public void setMembershipstartdate(String MembershipStartDate) {
        this.MembershipStartDate = MembershipStartDate;
    }
    public String getPromocode() {
        return PromoCode;
    }

    public void setPromocode(String PromoCode) {
        this.PromoCode = PromoCode;
    }


}