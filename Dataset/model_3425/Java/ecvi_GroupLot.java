





import java.util.List;
import java.util.ArrayList;

public class ecvi_GroupLot  {

    private String sexDetail;
    private String breed;
    private String sex;
    private String unit;
    private String quantity;
    private String description;
    private String age;
    private String species;





    private ecvi_Ecvi ecvi_ecvi;


    public ecvi_GroupLot(
        String sexDetail,        String breed,        String sex,        String unit,        String quantity,        String description,        String age,        String species    ) {
        this.sexDetail = sexDetail;
        this.breed = breed;
        this.sex = sex;
        this.unit = unit;
        this.quantity = quantity;
        this.description = description;
        this.age = age;
        this.species = species;
    }


    public String getSexdetail() {
        return sexDetail;
    }

    public void setSexdetail(String sexDetail) {
        this.sexDetail = sexDetail;
    }
    public String getBreed() {
        return breed;
    }

    public void setBreed(String breed) {
        this.breed = breed;
    }
    public String getSex() {
        return sex;
    }

    public void setSex(String sex) {
        this.sex = sex;
    }
    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }
    public String getQuantity() {
        return quantity;
    }

    public void setQuantity(String quantity) {
        this.quantity = quantity;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getAge() {
        return age;
    }

    public void setAge(String age) {
        this.age = age;
    }
    public String getSpecies() {
        return species;
    }

    public void setSpecies(String species) {
        this.species = species;
    }

    public ecvi_Ecvi getEcvi_ecvi() {
        return ecvi_ecvi;
    }

    public void setEcvi_ecvi(ecvi_Ecvi ecvi_ecvi) {
        this.ecvi_ecvi = ecvi_ecvi;
    }

}