





import java.util.List;
import java.util.ArrayList;

public class Material  {

    private String Material_name;
    private String Unit;
    private String Stock;
    private String Stock1;
    private int Material_id;



    public Material(
        String Material_name,        String Unit,        String Stock,        String Stock1,        int Material_id    ) {
        this.Material_name = Material_name;
        this.Unit = Unit;
        this.Stock = Stock;
        this.Stock1 = Stock1;
        this.Material_id = Material_id;
    }


    public String getMaterial_name() {
        return Material_name;
    }

    public void setMaterial_name(String Material_name) {
        this.Material_name = Material_name;
    }
    public String getUnit() {
        return Unit;
    }

    public void setUnit(String Unit) {
        this.Unit = Unit;
    }
    public String getStock() {
        return Stock;
    }

    public void setStock(String Stock) {
        this.Stock = Stock;
    }
    public String getStock1() {
        return Stock1;
    }

    public void setStock1(String Stock1) {
        this.Stock1 = Stock1;
    }
    public int getMaterial_id() {
        return Material_id;
    }

    public void setMaterial_id(int Material_id) {
        this.Material_id = Material_id;
    }


}