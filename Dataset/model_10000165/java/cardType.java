





import java.util.List;
import java.util.ArrayList;

public class cardType  {

    private None Heart;
    private None Diamond;
    private None Spades;
    private None club;



    public cardType(
        None Heart,        None Diamond,        None Spades,        None club    ) {
        this.Heart = Heart;
        this.Diamond = Diamond;
        this.Spades = Spades;
        this.club = club;
    }


    public None getHeart() {
        return Heart;
    }

    public void setHeart(None Heart) {
        this.Heart = Heart;
    }
    public None getDiamond() {
        return Diamond;
    }

    public void setDiamond(None Diamond) {
        this.Diamond = Diamond;
    }
    public None getSpades() {
        return Spades;
    }

    public void setSpades(None Spades) {
        this.Spades = Spades;
    }
    public None getClub() {
        return club;
    }

    public void setClub(None club) {
        this.club = club;
    }


}