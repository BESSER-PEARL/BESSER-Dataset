





import java.util.List;
import java.util.ArrayList;

public class SWRC_Misc extends Publication {

    private String howpublished;
    private String month;



    public SWRC_Misc(
        String howpublished,        String month    ) {
        super(
        );
        this.howpublished = howpublished;
        this.month = month;
    }


    public String getHowpublished() {
        return howpublished;
    }

    public void setHowpublished(String howpublished) {
        this.howpublished = howpublished;
    }
    public String getMonth() {
        return month;
    }

    public void setMonth(String month) {
        this.month = month;
    }


}