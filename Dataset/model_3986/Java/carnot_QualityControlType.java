





import java.util.List;
import java.util.ArrayList;

public class carnot_QualityControlType  {






    private List<carnot_Code> carnot_codes;




    private carnot_ModelType carnot_modeltype;


    public carnot_QualityControlType(
    ) {
        this.carnot_codes = new ArrayList<>();
    }

    public carnot_QualityControlType(
        ArrayList<carnot_Code> carnot_codes    ) {
        this.carnot_codes = carnot_codes;
    }


    public List<carnot_Code> getCarnot_codes() {
        return carnot_codes;
    }

    public void addCarnot_code(Carnot_code carnot_code) {
        this.carnot_codes.add(carnot_code);
    }
    public carnot_ModelType getCarnot_modeltype() {
        return carnot_modeltype;
    }

    public void setCarnot_modeltype(carnot_ModelType carnot_modeltype) {
        this.carnot_modeltype = carnot_modeltype;
    }

}