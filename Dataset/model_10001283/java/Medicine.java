





import java.util.List;
import java.util.ArrayList;

public class Medicine  {

    private String ActiveIngredient;
    private int ID;
    private String name;
    private String Price;
    private String Type;





    private Diagnosis diagnosis;


    public Medicine(
        String ActiveIngredient,        int ID,        String name,        String Price,        String Type    ) {
        this.ActiveIngredient = ActiveIngredient;
        this.ID = ID;
        this.name = name;
        this.Price = Price;
        this.Type = Type;
    }


    public String getActiveingredient() {
        return ActiveIngredient;
    }

    public void setActiveingredient(String ActiveIngredient) {
        this.ActiveIngredient = ActiveIngredient;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPrice() {
        return Price;
    }

    public void setPrice(String Price) {
        this.Price = Price;
    }
    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }

    public Diagnosis getDiagnosis() {
        return diagnosis;
    }

    public void setDiagnosis(Diagnosis diagnosis) {
        this.diagnosis = diagnosis;
    }

}