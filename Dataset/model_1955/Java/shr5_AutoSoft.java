





import java.util.List;
import java.util.ArrayList;

public class shr5_AutoSoft extends RiggerProgram {

    private int rating;





    private shr5_Drohne shr5_drohne;


    public shr5_AutoSoft(
        int rating    ) {
        super(
        );
        this.rating = rating;
    }


    public int getRating() {
        return rating;
    }

    public void setRating(int rating) {
        this.rating = rating;
    }

    public shr5_Drohne getShr5_drohne() {
        return shr5_drohne;
    }

    public void setShr5_drohne(shr5_Drohne shr5_drohne) {
        this.shr5_drohne = shr5_drohne;
    }

}