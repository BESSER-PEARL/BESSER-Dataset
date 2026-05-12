





import java.util.List;
import java.util.ArrayList;

public class Medicine  {

    private String Price;
    private String ActiveIngredient;
    private String Type;
    private String name;
    private int ID;





    private Diagnosis diagnosis;


    public Medicine(
        String Price,        String ActiveIngredient,        String Type,        String name,        int ID    ) {
        this.Price = Price;
        this.ActiveIngredient = ActiveIngredient;
        this.Type = Type;
        this.name = name;
        this.ID = ID;
    }


    public String getPrice() {
        return Price;
    }

    public void setPrice(String Price) {
        this.Price = Price;
    }
    public String getActiveingredient() {
        return ActiveIngredient;
    }

    public void setActiveingredient(String ActiveIngredient) {
        this.ActiveIngredient = ActiveIngredient;
    }
    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }

    public Diagnosis getDiagnosis() {
        return diagnosis;
    }

    public void setDiagnosis(Diagnosis diagnosis) {
        this.diagnosis = diagnosis;
    }

}