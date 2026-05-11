





import java.util.List;
import java.util.ArrayList;

public class shr5Management_LifestyleToStartMoney  {

    private int numberOfW;
    private int moneyFactor;





    private shr5Management_CharacterGeneratorSystem shr5management_charactergeneratorsystem;




    private List<shr5Management_Lifestyle> shr5management_lifestyles;


    public shr5Management_LifestyleToStartMoney(
        int numberOfW,        int moneyFactor    ) {
        this.numberOfW = numberOfW;
        this.moneyFactor = moneyFactor;
        this.shr5management_lifestyles = new ArrayList<>();
    }

    public shr5Management_LifestyleToStartMoney(
        int numberOfW,        int moneyFactor        ArrayList<shr5Management_Lifestyle> shr5management_lifestyles    ) {
        this.numberOfW = numberOfW;
        this.moneyFactor = moneyFactor;
        this.shr5management_lifestyles = shr5management_lifestyles;
    }

    public int getNumberofw() {
        return numberOfW;
    }

    public void setNumberofw(int numberOfW) {
        this.numberOfW = numberOfW;
    }
    public int getMoneyfactor() {
        return moneyFactor;
    }

    public void setMoneyfactor(int moneyFactor) {
        this.moneyFactor = moneyFactor;
    }

    public shr5Management_CharacterGeneratorSystem getShr5management_charactergeneratorsystem() {
        return shr5management_charactergeneratorsystem;
    }

    public void setShr5management_charactergeneratorsystem(shr5Management_CharacterGeneratorSystem shr5management_charactergeneratorsystem) {
        this.shr5management_charactergeneratorsystem = shr5management_charactergeneratorsystem;
    }
    public List<shr5Management_Lifestyle> getShr5management_lifestyles() {
        return shr5management_lifestyles;
    }

    public void addShr5management_lifestyle(Shr5management_lifestyle shr5management_lifestyle) {
        this.shr5management_lifestyles.add(shr5management_lifestyle);
    }

}