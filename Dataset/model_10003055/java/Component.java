





import java.util.List;
import java.util.ArrayList;

public class Component  {

    private float prijs;
    private String type;
    private String model;
    private float beschikbaarheidspercentage;



    public Component(
        float prijs,        String type,        String model,        float beschikbaarheidspercentage    ) {
        this.prijs = prijs;
        this.type = type;
        this.model = model;
        this.beschikbaarheidspercentage = beschikbaarheidspercentage;
    }


    public float getPrijs() {
        return prijs;
    }

    public void setPrijs(float prijs) {
        this.prijs = prijs;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        this.model = model;
    }
    public float getBeschikbaarheidspercentage() {
        return beschikbaarheidspercentage;
    }

    public void setBeschikbaarheidspercentage(float beschikbaarheidspercentage) {
        this.beschikbaarheidspercentage = beschikbaarheidspercentage;
    }


}