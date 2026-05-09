





import java.util.List;
import java.util.ArrayList;

public class shr5_AbstaktWaffe extends AbstraktGegenstand {

    private String schadenscode;
    private String schadesTyp;
    private int praezision;
    private int durchschlagsKraft;





    private shr5_AutoSoft shr5_autosoft;




    private shr5_WeaponMount shr5_weaponmount;




    private shr5_CyberImplantWeapon shr5_cyberimplantweapon;


    public shr5_AbstaktWaffe(
        String schadenscode,        String schadesTyp,        int praezision,        int durchschlagsKraft    ) {
        super(
        );
        this.schadenscode = schadenscode;
        this.schadesTyp = schadesTyp;
        this.praezision = praezision;
        this.durchschlagsKraft = durchschlagsKraft;
    }


    public String getSchadenscode() {
        return schadenscode;
    }

    public void setSchadenscode(String schadenscode) {
        this.schadenscode = schadenscode;
    }
    public String getSchadestyp() {
        return schadesTyp;
    }

    public void setSchadestyp(String schadesTyp) {
        this.schadesTyp = schadesTyp;
    }
    public int getPraezision() {
        return praezision;
    }

    public void setPraezision(int praezision) {
        this.praezision = praezision;
    }
    public int getDurchschlagskraft() {
        return durchschlagsKraft;
    }

    public void setDurchschlagskraft(int durchschlagsKraft) {
        this.durchschlagsKraft = durchschlagsKraft;
    }

    public shr5_AutoSoft getShr5_autosoft() {
        return shr5_autosoft;
    }

    public void setShr5_autosoft(shr5_AutoSoft shr5_autosoft) {
        this.shr5_autosoft = shr5_autosoft;
    }
    public shr5_WeaponMount getShr5_weaponmount() {
        return shr5_weaponmount;
    }

    public void setShr5_weaponmount(shr5_WeaponMount shr5_weaponmount) {
        this.shr5_weaponmount = shr5_weaponmount;
    }
    public shr5_CyberImplantWeapon getShr5_cyberimplantweapon() {
        return shr5_cyberimplantweapon;
    }

    public void setShr5_cyberimplantweapon(shr5_CyberImplantWeapon shr5_cyberimplantweapon) {
        this.shr5_cyberimplantweapon = shr5_cyberimplantweapon;
    }

}