





import java.util.List;
import java.util.ArrayList;

public class Patient_Check_In_aDoctor  {

    private String Rank;
    private int ID;
    private String Specialization;
    private String Name;



    public Patient_Check_In_aDoctor(
        String Rank,        int ID,        String Specialization,        String Name    ) {
        this.Rank = Rank;
        this.ID = ID;
        this.Specialization = Specialization;
        this.Name = Name;
    }


    public String getRank() {
        return Rank;
    }

    public void setRank(String Rank) {
        this.Rank = Rank;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }
    public String getSpecialization() {
        return Specialization;
    }

    public void setSpecialization(String Specialization) {
        this.Specialization = Specialization;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }


}