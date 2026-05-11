





import java.util.List;
import java.util.ArrayList;

public class MARTE_HwLayout_HwComponent extends HwResource {

    private String r_Conditions;
    private String grid;
    private String position;
    private String weight;
    private String staticDissipation;
    private String kind;
    private String nbPins;
    private String staticConsumption;
    private String area;
    private String price;
    private String dimensions;



    public MARTE_HwLayout_HwComponent(
        String r_Conditions,        String grid,        String position,        String weight,        String staticDissipation,        String kind,        String nbPins,        String staticConsumption,        String area,        String price,        String dimensions    ) {
        super(
        );
        this.r_Conditions = r_Conditions;
        this.grid = grid;
        this.position = position;
        this.weight = weight;
        this.staticDissipation = staticDissipation;
        this.kind = kind;
        this.nbPins = nbPins;
        this.staticConsumption = staticConsumption;
        this.area = area;
        this.price = price;
        this.dimensions = dimensions;
    }


    public String getR_conditions() {
        return r_Conditions;
    }

    public void setR_conditions(String r_Conditions) {
        this.r_Conditions = r_Conditions;
    }
    public String getGrid() {
        return grid;
    }

    public void setGrid(String grid) {
        this.grid = grid;
    }
    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }
    public String getWeight() {
        return weight;
    }

    public void setWeight(String weight) {
        this.weight = weight;
    }
    public String getStaticdissipation() {
        return staticDissipation;
    }

    public void setStaticdissipation(String staticDissipation) {
        this.staticDissipation = staticDissipation;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }
    public String getNbpins() {
        return nbPins;
    }

    public void setNbpins(String nbPins) {
        this.nbPins = nbPins;
    }
    public String getStaticconsumption() {
        return staticConsumption;
    }

    public void setStaticconsumption(String staticConsumption) {
        this.staticConsumption = staticConsumption;
    }
    public String getArea() {
        return area;
    }

    public void setArea(String area) {
        this.area = area;
    }
    public String getPrice() {
        return price;
    }

    public void setPrice(String price) {
        this.price = price;
    }
    public String getDimensions() {
        return dimensions;
    }

    public void setDimensions(String dimensions) {
        this.dimensions = dimensions;
    }


}