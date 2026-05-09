





import java.util.List;
import java.util.ArrayList;

public class shr5_Munition extends AbstraktGegenstand, Menge {

    private int armorMod;
    private int damageMod;
    private String damageType;



    public shr5_Munition(
        int armorMod,        int damageMod,        String damageType    ) {
        super(
        );
        this.armorMod = armorMod;
        this.damageMod = damageMod;
        this.damageType = damageType;
    }


    public int getArmormod() {
        return armorMod;
    }

    public void setArmormod(int armorMod) {
        this.armorMod = armorMod;
    }
    public int getDamagemod() {
        return damageMod;
    }

    public void setDamagemod(int damageMod) {
        this.damageMod = damageMod;
    }
    public String getDamagetype() {
        return damageType;
    }

    public void setDamagetype(String damageType) {
        this.damageType = damageType;
    }


}