





import java.util.List;
import java.util.ArrayList;

public class shadowrun_Reichweite extends Beschreibbar {

    private int reichweiteWeit;
    private int reichweiteKurz;
    private int reichweiteMittel1;
    private int reichweiteExtrem1;
    private int reichweiteMittel;
    private int reichweiteExtrem;
    private int reichweiteKurz1;
    private int reichweiteWeit1;





    private shadowrun_AbstaktFernKampfwaffe shadowrun_abstaktfernkampfwaffe;


    public shadowrun_Reichweite(
        int reichweiteWeit,        int reichweiteKurz,        int reichweiteMittel1,        int reichweiteExtrem1,        int reichweiteMittel,        int reichweiteExtrem,        int reichweiteKurz1,        int reichweiteWeit1    ) {
        super(
        );
        this.reichweiteWeit = reichweiteWeit;
        this.reichweiteKurz = reichweiteKurz;
        this.reichweiteMittel1 = reichweiteMittel1;
        this.reichweiteExtrem1 = reichweiteExtrem1;
        this.reichweiteMittel = reichweiteMittel;
        this.reichweiteExtrem = reichweiteExtrem;
        this.reichweiteKurz1 = reichweiteKurz1;
        this.reichweiteWeit1 = reichweiteWeit1;
    }


    public int getReichweiteweit() {
        return reichweiteWeit;
    }

    public void setReichweiteweit(int reichweiteWeit) {
        this.reichweiteWeit = reichweiteWeit;
    }
    public int getReichweitekurz() {
        return reichweiteKurz;
    }

    public void setReichweitekurz(int reichweiteKurz) {
        this.reichweiteKurz = reichweiteKurz;
    }
    public int getReichweitemittel1() {
        return reichweiteMittel1;
    }

    public void setReichweitemittel1(int reichweiteMittel1) {
        this.reichweiteMittel1 = reichweiteMittel1;
    }
    public int getReichweiteextrem1() {
        return reichweiteExtrem1;
    }

    public void setReichweiteextrem1(int reichweiteExtrem1) {
        this.reichweiteExtrem1 = reichweiteExtrem1;
    }
    public int getReichweitemittel() {
        return reichweiteMittel;
    }

    public void setReichweitemittel(int reichweiteMittel) {
        this.reichweiteMittel = reichweiteMittel;
    }
    public int getReichweiteextrem() {
        return reichweiteExtrem;
    }

    public void setReichweiteextrem(int reichweiteExtrem) {
        this.reichweiteExtrem = reichweiteExtrem;
    }
    public int getReichweitekurz1() {
        return reichweiteKurz1;
    }

    public void setReichweitekurz1(int reichweiteKurz1) {
        this.reichweiteKurz1 = reichweiteKurz1;
    }
    public int getReichweiteweit1() {
        return reichweiteWeit1;
    }

    public void setReichweiteweit1(int reichweiteWeit1) {
        this.reichweiteWeit1 = reichweiteWeit1;
    }

    public shadowrun_AbstaktFernKampfwaffe getShadowrun_abstaktfernkampfwaffe() {
        return shadowrun_abstaktfernkampfwaffe;
    }

    public void setShadowrun_abstaktfernkampfwaffe(shadowrun_AbstaktFernKampfwaffe shadowrun_abstaktfernkampfwaffe) {
        this.shadowrun_abstaktfernkampfwaffe = shadowrun_abstaktfernkampfwaffe;
    }

}