





import java.util.List;
import java.util.ArrayList;

public class Pets  {

    private String PetType;
    private int Age;
    private String PetName;
    private int PetID;



    public Pets(
        String PetType,        int Age,        String PetName,        int PetID    ) {
        this.PetType = PetType;
        this.Age = Age;
        this.PetName = PetName;
        this.PetID = PetID;
    }


    public String getPettype() {
        return PetType;
    }

    public void setPettype(String PetType) {
        this.PetType = PetType;
    }
    public int getAge() {
        return Age;
    }

    public void setAge(int Age) {
        this.Age = Age;
    }
    public String getPetname() {
        return PetName;
    }

    public void setPetname(String PetName) {
        this.PetName = PetName;
    }
    public int getPetid() {
        return PetID;
    }

    public void setPetid(int PetID) {
        this.PetID = PetID;
    }


}