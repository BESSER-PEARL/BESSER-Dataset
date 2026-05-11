





import java.util.List;
import java.util.ArrayList;

public class shr5Management_Changes  {

    private int karmaCost;
    private boolean changeApplied;
    private String date;
    private String dateApplied;





    private shr5Management_ManagedCharacter shr5management_managedcharacter;




    private shr5Management_ManagedCharacter shr5management_managedcharacter;




    private shr5Management_CharacterChange shr5management_characterchange;


    public shr5Management_Changes(
        int karmaCost,        boolean changeApplied,        String date,        String dateApplied    ) {
        this.karmaCost = karmaCost;
        this.changeApplied = changeApplied;
        this.date = date;
        this.dateApplied = dateApplied;
    }


    public int getKarmacost() {
        return karmaCost;
    }

    public void setKarmacost(int karmaCost) {
        this.karmaCost = karmaCost;
    }
    public boolean getChangeapplied() {
        return changeApplied;
    }

    public void setChangeapplied(boolean changeApplied) {
        this.changeApplied = changeApplied;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public String getDateapplied() {
        return dateApplied;
    }

    public void setDateapplied(String dateApplied) {
        this.dateApplied = dateApplied;
    }

    public shr5Management_ManagedCharacter getShr5management_managedcharacter() {
        return shr5management_managedcharacter;
    }

    public void setShr5management_managedcharacter(shr5Management_ManagedCharacter shr5management_managedcharacter) {
        this.shr5management_managedcharacter = shr5management_managedcharacter;
    }
    public shr5Management_ManagedCharacter getShr5management_managedcharacter() {
        return shr5management_managedcharacter;
    }

    public void setShr5management_managedcharacter(shr5Management_ManagedCharacter shr5management_managedcharacter) {
        this.shr5management_managedcharacter = shr5management_managedcharacter;
    }
    public shr5Management_CharacterChange getShr5management_characterchange() {
        return shr5management_characterchange;
    }

    public void setShr5management_characterchange(shr5Management_CharacterChange shr5management_characterchange) {
        this.shr5management_characterchange = shr5management_characterchange;
    }

}