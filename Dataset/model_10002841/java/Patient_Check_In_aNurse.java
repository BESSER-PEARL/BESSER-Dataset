





import java.util.List;
import java.util.ArrayList;

public class Patient_Check_In_aNurse  {

    private int ID;
    private String Ranking;
    private String Name;



    public Patient_Check_In_aNurse(
        int ID,        String Ranking,        String Name    ) {
        this.ID = ID;
        this.Ranking = Ranking;
        this.Name = Name;
    }


    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }
    public String getRanking() {
        return Ranking;
    }

    public void setRanking(String Ranking) {
        this.Ranking = Ranking;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }


}