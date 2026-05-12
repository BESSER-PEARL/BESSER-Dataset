





import java.util.List;
import java.util.ArrayList;

public class Online_Shopping_Card_Payment  {

    private String Valid_Date;
    private String Card_Holder_Name;
    private int CVS_Number;
    private int Card_Number;



    public Online_Shopping_Card_Payment(
        String Valid_Date,        String Card_Holder_Name,        int CVS_Number,        int Card_Number    ) {
        this.Valid_Date = Valid_Date;
        this.Card_Holder_Name = Card_Holder_Name;
        this.CVS_Number = CVS_Number;
        this.Card_Number = Card_Number;
    }


    public String getValid_date() {
        return Valid_Date;
    }

    public void setValid_date(String Valid_Date) {
        this.Valid_Date = Valid_Date;
    }
    public String getCard_holder_name() {
        return Card_Holder_Name;
    }

    public void setCard_holder_name(String Card_Holder_Name) {
        this.Card_Holder_Name = Card_Holder_Name;
    }
    public int getCvs_number() {
        return CVS_Number;
    }

    public void setCvs_number(int CVS_Number) {
        this.CVS_Number = CVS_Number;
    }
    public int getCard_number() {
        return Card_Number;
    }

    public void setCard_number(int Card_Number) {
        this.Card_Number = Card_Number;
    }


}