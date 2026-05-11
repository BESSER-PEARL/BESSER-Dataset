





import java.util.List;
import java.util.ArrayList;

public class shr5Management_ManagedCharacter  {

    private int notorietyBasic;
    private String sex;
    private int weight;
    private int streetCred;
    private int notoriety;
    private int height;
    private String dateofbirth;
    private int currentKarma;
    private int karmaGaint;
    private int publicAwareness;





    private shr5Management_CharacterGenerator shr5management_charactergenerator;




    private shr5Management_CharacterGroup shr5management_charactergroup;


    public shr5Management_ManagedCharacter(
        int notorietyBasic,        String sex,        int weight,        int streetCred,        int notoriety,        int height,        String dateofbirth,        int currentKarma,        int karmaGaint,        int publicAwareness    ) {
        this.notorietyBasic = notorietyBasic;
        this.sex = sex;
        this.weight = weight;
        this.streetCred = streetCred;
        this.notoriety = notoriety;
        this.height = height;
        this.dateofbirth = dateofbirth;
        this.currentKarma = currentKarma;
        this.karmaGaint = karmaGaint;
        this.publicAwareness = publicAwareness;
    }


    public int getNotorietybasic() {
        return notorietyBasic;
    }

    public void setNotorietybasic(int notorietyBasic) {
        this.notorietyBasic = notorietyBasic;
    }
    public String getSex() {
        return sex;
    }

    public void setSex(String sex) {
        this.sex = sex;
    }
    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }
    public int getStreetcred() {
        return streetCred;
    }

    public void setStreetcred(int streetCred) {
        this.streetCred = streetCred;
    }
    public int getNotoriety() {
        return notoriety;
    }

    public void setNotoriety(int notoriety) {
        this.notoriety = notoriety;
    }
    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }
    public String getDateofbirth() {
        return dateofbirth;
    }

    public void setDateofbirth(String dateofbirth) {
        this.dateofbirth = dateofbirth;
    }
    public int getCurrentkarma() {
        return currentKarma;
    }

    public void setCurrentkarma(int currentKarma) {
        this.currentKarma = currentKarma;
    }
    public int getKarmagaint() {
        return karmaGaint;
    }

    public void setKarmagaint(int karmaGaint) {
        this.karmaGaint = karmaGaint;
    }
    public int getPublicawareness() {
        return publicAwareness;
    }

    public void setPublicawareness(int publicAwareness) {
        this.publicAwareness = publicAwareness;
    }

    public shr5Management_CharacterGenerator getShr5management_charactergenerator() {
        return shr5management_charactergenerator;
    }

    public void setShr5management_charactergenerator(shr5Management_CharacterGenerator shr5management_charactergenerator) {
        this.shr5management_charactergenerator = shr5management_charactergenerator;
    }
    public shr5Management_CharacterGroup getShr5management_charactergroup() {
        return shr5management_charactergroup;
    }

    public void setShr5management_charactergroup(shr5Management_CharacterGroup shr5management_charactergroup) {
        this.shr5management_charactergroup = shr5management_charactergroup;
    }

}